import distro, math
from scipy.optimize import fsolve
from scipy.stats import reciprocal

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    equations = lambda (a, b): ( float(reciprocal.stats(a,b,moments='m'))-mu , float(reciprocal.stats(a,b,moments='v'))-sig2 )
    a , b = fsolve(equations, (1,2))
    return (a, b)

        

distro.register(
    name        = 'Reciprocal',
    domain      = distro.Domain.Continuous,
    params      = ('a','b'),
    paramSolver = _solver,
    cdf         = lambda x, m, s : 0.5*(1+(x-m)/s+1/math.pi*math.sin((x-m)/s*math.pi)),
    sample      = lambda m, s = 0 : reciprocal.rvs(a,b),
    fittingFns  = {
        distro.Stat.Skew: lambda a, b : float(reciprocal.stats(a,b,moments='s')),
        distro.Stat.Kurt: lambda a, b : float(reciprocal.stats(a,b,moments='k'))+3
    }
)
