import distro, numpy

def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    return (1.0 / mu,)

distro.register(
    name        = 'Exponential',
    domain      = distro.Domain.Continuous,
    params      = ('lambda', ),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda lamb : numpy.random.exponential(1.0/lamb), 
    fittingFns  = {
        distro.Stat.Sig2: lambda lamb : 1.0 / lamb ** 2,
        distro.Stat.Skew: lambda lamb : 2.0,
        distro.Stat.Kurt: lambda lamb : 9.0
    }
)
