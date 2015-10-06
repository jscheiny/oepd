import distro, utils, numpy

def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    return (1.0 / mu,)

def _variance(p):
    return (1.0 - p)/p**2

def _skewness(p):
    return (2.0-p)/pow(1-p,0.5)

def _kurtosis(a, b):
    return 6 + p**2/(1.0 - p) + 3

distro.register(
    name        = 'Geometric',
    domain      = distro.Domain.Discrete,
    params      = ('p',),
    paramSolver = _solver,
    cdf         = lambda k : 1 - (1.0 - p)**k,
    sample      = lambda p : numpy.random.geometric(p), # unimplemented
    fittingFns  = {
        distro.Stat.Sig2: _variance,
        distro.Stat.Skew: _skewness,
        distro.Stat.Kurt: _kurtosis
    }
)
