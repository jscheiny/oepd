import distro, math, numpy 


def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    m = mu
    s = math.sqrt(3*sig2/math.pi**2)    
    return (m,s)

distro.register(
    name        = 'Logistic',
    domain      = distro.Domain.Continuous,
    params      = ('m','s'),
    paramSolver = _solver,
    cdf         = lambda x, m, s : 1/(1+math.exp(-(x-m)/s)),
    sample      = lambda m, s: numpy.random.logistic(m,s),
    fittingFns  = {
        distro.Stat.Skew: lambda m,s : 0,
        distro.Stat.Kurt: lambda m,s : 1.2+3,
        distro.Stat.Med:  lambda m,s : m
    }
)


