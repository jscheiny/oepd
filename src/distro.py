import asserts, errors, bisect, math

class Domain(object):
    Continuous = 'Continuous'
    Discrete   = 'Discrete'

class Stat(object):
    Mu = 'mu'
    Sig2 = 'sig2'
    Skew = 'skew'
    Kurt = 'kurt'
    Med = 'med'
    Max = 'maximum'
    Min = 'minimum'

class Fit(object):
    Great = 3
    Good = 2
    Decent = 1
    Trivial = 0
    NoFit = -1

def _scoreFits(fitList):
    """
    Given a set of fittings returned by _approxEqual, returns a fitting rating,
    a value of the Fit enum.
    """
    if len(fitList) == 0:
        return Fit.Trivial
    if min(fitList) == 1 or fitList.count(2)>1:
        return Fit.NoFit
    if min(fitList)==2:
        return Fit.Decent
    if min(fitList) == 3:
        if fitList.count(3)==1 and len(fitList)>1:
            return Fit.Good
        else:
            return Fit.Decent
    if min(fitList) == 4 and len(fitList) <= 2:
        return Fit.Good
    return Fit.Great

def _approxEqual(a,b):
    """
    Returns a rating of how close a and b are to each other, 5 = great, 1 = bad.
    """
    if a<0 and b<0:
        a = -a
        b = -b
    if b<a:
        a,b = b,a
    if a==b:
        return 5
    if a*b<=0:
        s = round(-math.log(abs(a)+abs(b)))
    else:
        s = round(-math.log( abs(b-a)/float(a)) )
    if s<=0:
        return 1
    if s>5:
        return 5
    return int(s)

class _Distribution(object):
    def __init__(self, name, domain, params, paramSolver, cdf, sample, fittingFns):
        """
        Creates a reference representation of a probability distribution.

        Args:
            name:
                A string containing the name of the distribution
            domain:
                One of the enumeration types drawn from the Domain type
            params:
                A tuple of strings containing the names of all of the parameters
                of this distribution. The order of params here determines the
                order in which they will be passed to all relevant functions.
            paramSolver:
                A function which takes a map from descriptive stats to their values
                and returns a tuple containing the values of the parameters for the
                distribution based on those stats (should be returned in the same
                order as given in the params argument). If it is unsolvable with
                the given data, it should return either None or throw an
                UnsolvableParamsError.
            cdf:
                A cdf function which should take two arguments, an value and
                a tuple of distribution parameters.
            sample:
                A real-valued function which takes len(params) arguments and returns a random
                instance of this random variable
            fittingFns:
                A map from descriptive stats to functions that take a set of parameter
                values, and return the value of that stat for the PD. These are
                the functions used to determine if this PD is a good fit for the data.

        """
        asserts.checkType(name, str)
        asserts.checkIterType(params, str, iterType = tuple)
        asserts.checkCallable(paramSolver)
        asserts.checkCallable(cdf)
        asserts.checkCallable(sample)
        # TODO: Check type of fittingFns

        self.name = name
        self.domain = domain
        self.params = params
        self.paramSolver = paramSolver
        self.cdf = cdf
        self.sample = sample
        self.fittingFns = fittingFns

    def __repr__(self):
        r = self.domain + ' Probability Distribution'
        r += ': ' + self.name
        if len(self.params) > 0:
            r += '(' + (', '.join(self.params)) + ')'
        return r

    def goodnessOfFit(self, **values):
        params = None
        try:
            params = self.paramSolver(values)
        except errors.UnsolvableParamsError as e:
            return Fit.NoFit
        if params == None:
            return Fit.NoFit

        fitList = []
        for stat, fitFn in self.fittingFns.iteritems():
            if stat in values:
                fit = _approxEqual(values[stat], fitFn(*params))
                fitList.append(fit)
        return _scoreFits(fitList), dict(zip(self.params, params))

def extractStats(statsMap, stats, noneWhenMissing = False):
    extracted = []
    for stat in stats:
        if stat not in statsMap:
            if noneWhenMissing:
                extracted.append(None)
            else:
                raise errors.UnsolvableParamsError.missingStat(stat)
        else:
            extracted.append(statsMap[stat])
    return tuple(extracted)

_distros = {}

def register(**args):
    distro = _Distribution(**args)
    name = args['name']
    _distros[name] = distro
    return distro

def find(name):
    if name in _distros:
        return _distros[name]
    return None

def matches(domain, **statValues):
    results = []
    for name, d in _distros.iteritems():
        if d.domain == domain:
            try:
                (fit, params) = d.goodnessOfFit(**statValues)
                if fit != Fit.NoFit:
                    results.append((fit, d, params))
            except:
                pass
    return results
