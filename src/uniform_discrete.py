import distro, utils

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, distro.Stat.Mu, distro.Stat.Sig2)
    roots = utils.solve_quadratic_eqn(1, -2 * mu - 1, mu ** 2 + mu - 3 * sig2)
    if roots == None:
        return None
    else:
        a = min(roots)
        b = 2 * mu - a
        return (a, b)

def _kurtosis(a, b):
    n = b - a + 1.0 
    return -6 * (n ** 2 + 1) / 5. / (n ** 2 - 1)

uniform = distro.Distribution(
    name        = 'Uniform Discrete',
    domain      = distro.Domain.Discrete,
    params      = ('a', 'b'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    fittingFns  = {
        distro.Stat.Skew: lambda a, b : 0,
        distro.Stat.Kurt: _kurtosis
    }
)