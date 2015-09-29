import enum

class Domain(enum.Enum):
    Continuous = 'Continuous'
    Discrete   = 'Discrete'

class Distribution(object):
    def __init__(self, domain, cdf, solver, params = (), name = None):
        """
        Creates a reference representation of a probability distribution.

        Args:
            domain:
                One of the enumeration types drawn from the Domain type
            cdf:
                A cdf function which should take two arguments, an value and
                a tuple of distribution parameters.
            solver:
                A function which takes a set of descriptive stats and returns a
                tuple containing the values of the parameters for the distribution
                based on those stats.
            params:
                A tuple of strings containing the names of all of the parameters
                of this distribution. The order of params here determines the
                order in which they will be passed to all relevant functions.
            name:
                A string containing the name of the distribution (may be None).
        """
        assert type(domain) == Domain
        assert type(params) == tuple
        for p in params:
            assert type(p) == str
        assert callable(cdf)
        assert callable(solver)
        assert name == None or type(name) == str
        self.domain = domain
        self.params = params
        self.name = name

    def __repr__(self):
        r = self.domain.value + ' Probability Distribution'
        if self.name != None and self.name != '':
            r += ': ' + self.name
        else:
            r += ' '
        if len(self.params) > 0:
            r += '(' + (', '.join(self.params)) + ')'
        return r