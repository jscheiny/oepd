import distro, numpy, random

def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    N = 2*mu
    return (N,)

distro.register(
    name        = 'Irwin_Hall',
    domain      = distro.Domain.Continuous,
    params      = ('N', ),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda N : sum([random.random() for i in xrange(N)]), 
    fittingFns  = {
        distro.Stat.Sig2: lambda N : N/12.,
        distro.Stat.Skew: lambda N : 0,
        distro.Stat.Kurt: lambda N : -1.2/N+3
    }
)
