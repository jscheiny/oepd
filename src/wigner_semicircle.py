import distro, math, numpy, random


def _solver(stats):
    (sig2,) = distro.extractStats(stats, [distro.Stat.Sig2])
    R = math.sqrt(4*sig2)
    return (R,)


distro.register(
    name        = 'Wigner_Semicircle', 
    domain      = distro.Domain.Continuous,
    params      = ('R',),  
    paramSolver = _solver,
    cdf         = lambda x, R : 0.5 + x*math.sqrt(R**2-x**2)/(math.pi*R**2) + math.asin(x/R)/math.pi,
    sample      = lambda R : 0, #not implemented
    fittingFns  = {
        distro.Stat.Mu: lambda   R : 0,        
        distro.Stat.Skew: lambda R : 0,
        distro.Stat.Kurt: lambda R : -1+3,
    }
)


