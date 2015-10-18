import distro, numpy, math
from scipy.stats import arcsine


def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    shift = mu - 0.5
    return (shift,)



distro.register(
    name        = 'Arcsine',
    domain      = distro.Domain.Continuous,
    params      = ('shift',),  #generalized slightly to r.v. X = arcsine + shift, where shift is a constant
    paramSolver = _solver,
    cdf         = lambda x : 2/math.pi*math.asin(math.sqrt(x)), 
    sample      = arcsine.rvs, 
    fittingFns  = {
        distro.Stat.Sig2: lambda : 0.125,
        distro.Stat.Skew: lambda :  0,
        distro.Stat.Kurt: lambda : -1.5+3
    }
)
