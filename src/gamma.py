import distro, math

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    theta = float(sig2) / mu
    k = float(mu) / theta
    return (k, theta)

distro.register(
    name        = 'Gamma',
    domain      = distro.Domain.Continuous,
    params      = ('k', 'theta'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    fittingFns  = {
        distro.Stat.Skew: lambda k, theta : 2 / math.sqrt(k),
        distro.Stat.Kurt: lambda k, theta : 6 / k + 3
    }
)
