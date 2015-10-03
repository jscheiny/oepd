import enum, asserts, utils, errors

class Domain(enum.Enum):
    Continuous = 'Continuous'
    Discrete   = 'Discrete'

class Stat(enum.Enum):
    Mu = 'mu'
    Sig2 = 'sig2'
    Skew = 'skew'
    Kurt = 'kurt'

    @staticmethod
    def lookup(value):
        for e in Stat:
            if e.value == value:
                return e
        return None

class Distribution(object):
    def __init__(self, name, domain, params, paramSolver, cdf, fittingFns):
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
                order as given in the params argument).
            cdf:
                A cdf function which should take two arguments, an value and
                a tuple of distribution parameters.
            fittingFns:
                A map from descriptive stats to functions that take a set of parameter
                values, and return the value of that stat for the PD. These are
                the functions used to determine if this PD is a good fit for the data.

        """
        asserts.checkType(name, str)
        asserts.checkType(domain, Domain)
        asserts.checkIterType(params, str, iterType = tuple)
        asserts.checkCallable(paramSolver)
        asserts.checkCallable(cdf)
        # TODO: Check type of fittingFns

        self.name = name
        self.domain = domain
        self.params = params
        self.paramSolver = paramSolver
        self.cdf = cdf
        self.fittingFns = fittingFns

    def __repr__(self):
        r = self.domain.value + ' Probability Distribution'
        r += ': ' + self.name
        if len(self.params) > 0:
            r += '(' + (', '.join(self.params)) + ')'
        return r

    def goodnessOfFit(self, **values):
        valueMap = {}
        for name, value in values.iteritems():
            stat = Stat.lookup(name)
            if name != None:
                valueMap[stat] = value

        params = self.paramSolver(valueMap)
        fitList = []
        for stat, fitFn in self.fittingFns.iteritems():
            if stat in valueMap:
                fit = utils.approx_equal(valueMap[stat], fitFn(*params))
                fitList.append(fit)
        return utils.fits2score(fitList)

def extractStats(statsMap, *stats):
    extracted = []
    for s in stats:
        if s not in statsMap:
            raise MissingStatError(s)
        extracted.append(statsMap[s])
    return tuple(extracted)
