import distro, math


def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    m = mu
    s = math.sqrt(sig2/(1./3 - 2/math.pi**2))
    return (m,s)
        


distro.register(
    name        = 'Raised_Cosine',
    domain      = distro.Domain.Continuous,
    params      = ('m','s'),
    paramSolver = _solver,
    cdf         = lambda x, m, s : (0.5*(1+(x-m)/s+1/math.pi*math.sin((x-m)/s*math.pi)) if abs(x-mu)<=s else 0),
    sample      = lambda m, s : 0,  #unimplemented
    fittingFns  = {
        distro.Stat.Skew: lambda m, s : 0,
        distro.Stat.Kurt: lambda m, s : 6*(90-math.pi**4)/(5*(math.pi**2-6)**2),
        distro.Stat.Med : lambda m, s : m
    }
)
