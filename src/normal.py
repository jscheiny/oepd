import distro, math, numpy

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    return (mu, math.sqrt(sig2))

distro.register(
    name        = 'Normal',
    domain      = distro.Domain.Continuous,
    params      = ('mu', 'sigma'),
    paramSolver = _solver,
    cdf         = lambda x, mu, sigma : 0.5*(1+math.erf((x-mu)/(sigma*math.sqrt(2)))), # unimplemented
    sample      = lambda mu, sigma: numpy.random.normal(mu,sigma),
    fittingFns  = {
        distro.Stat.Skew: lambda mu, sig : 0.0,
        distro.Stat.Kurt: lambda mu, sig : 3.0,
        distro.Stat.Med: lambda mu, sig: mu
    }
)
