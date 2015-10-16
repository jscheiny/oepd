import distro, math, numpy 


def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    m = mu
    b = math.sqrt(sig2/2) 
    return (m,b)

distro.register(
    name        = 'Laplace',
    domain      = distro.Domain.Continuous,
    params      = ('m','b'),
    paramSolver = _solver,
    cdf         = lambda x, m, b : (0.5*math.exp((x-m)/b) if x<m else 1-0.5*math.exp(-(x-m)/b)),
    sample      = lambda m, b: numpy.random.laplace(m, b),
    fittingFns  = {
        distro.Stat.Skew: lambda m,s : 0,
        distro.Stat.Kurt: lambda m,s : 3+3,
        distro.Stat.Med:  lambda m,s : m
    }
)


