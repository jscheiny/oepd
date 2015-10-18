import distro, math
from scipy.stats import maxwell


def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    a = mu/2*math.sqrt(math.pi/2)
    return (a,)

distro.register(
    name        = 'Maxwell_Boltzmann',
    domain      = distro.Domain.Continuous,
    params      = ('a', ),
    paramSolver = _solver,
    cdf         = lambda x, a : math.erf(x/(math.sqrt(2)*a))*math.sqrt(2/math.pi)*x*math.exp(-x**2/(2*a**a))/a ,
    sample      = lambda a : maxwell.rvs(scale=a), 
    fittingFns  = {
        distro.Stat.Sig2: lambda a : maxwell.stats(scale=a,moments='v'),
        distro.Stat.Skew: lambda a : maxwell.stats(scale=a,moments='s'),
        distro.Stat.Kurt: lambda a : maxwell.stats(scale=a,moments='k')+3
    }
)
