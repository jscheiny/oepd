import distro

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    return (mu, math.sqrt(sig2))

normal = distro.Distribution(
    name        = 'Normal',
    domain      = distro.Domain.Continuous,
    params      = ('mu', 'sigma'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    fittingFns  = {
        distro.Stat.Skew: lambda mu, sig : 0.0
        distro.Stat.Kurt: lambda mu, sig : 3.0
    }
)
