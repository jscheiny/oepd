import distro, numpy, math

from scipy.stats import arcsine

distro.register(
    name        = 'Arcsine',
    domain      = distro.Domain.Continuous,
    params      = (),
    #paramSolver = _solver,
    cdf         = lambda x : 2/math.pi*math.asin(math.sqrt(x)), 
    sample      = arcsine.rvs, 
    fittingFns  = {
        distro.Stat.Mu : lambda dummy : 0.5
        distro.Stat.Sig2: lambda dummy : 0.125,
        distro.Stat.Skew: lambda dummy :  0,
        distro.Stat.Kurt: lambda dummy : -1.5+3
    }
)
