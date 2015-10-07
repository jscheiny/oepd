import distro, numpy

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    lamb = mu/sig2
    k = lamb*mu
    return (k, lamb)

distro.register(
    name        = 'Erlang',
    domain      = distro.Domain.Continuous,
    params      = ('k','lambda'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda k, lamb : sum([numpy.random.exponential(1.0/lamb) for i in xrange(k)]), 
    fittingFns  = {
        distro.Stat.Skew: lambda lamb : 2.0/math.sqrt(k),
        distro.Stat.Kurt: lambda lamb : 6.0/k+3
    }
)
