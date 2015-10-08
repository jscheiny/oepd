import distro, math, numpy

def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    return (mu,)

distro.register(
    name        = 'Poisson',
    domain      = distro.Domain.Discrete,
    params      = ('lambda'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda lamb : numpy.random.poisson(lamb),
    fittingFns  = {
        distro.Stat.Sig2: lambda lamb : lamb,
        distro.Stat.Skew: lambda lamb : 1/math.sqrt(lamb),
        distro.Stat.Kurt: lambda n, p : 1.0/lamb+3
    }
)
