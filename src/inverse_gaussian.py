import distro, math, numpy


def _solver(stats): 
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    m = mu
    lamb =  m**3/sig2
    return (m, lamb)

distro.register(
    name        = 'Inverse_Gaussian', #also called Wald
    domain      = distro.Domain.Continuous,
    params      = ('m','lamb'),
    paramSolver = _solver,
    cdf         = lambda x, m, lamb : 0, #unimplemented
    sample      = lambda m, lamb: numpy.random.wald(mean=m, scale=lamb),
    fittingFns  = {
        distro.Stat.Skew: lambda m, lamb : 3*math.sqrt(m/lamb),
        distro.Stat.Kurt: lambda m, lamb : 15*m/lamb + 3
    }
)
