import distro, math
from scipy.optimize import fsolve
from scipy.stats import triang

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    equations = lambda (a, b): ( float(triang.stats(0,loc=a,scale=b-a,moments='m'))-mu , float(triang.stats(0,loc=a,scale=b-a,moments='v'))-sig2 )
    a , b = fsolve(equations, (mu-2*sig2,mu+3*sig2))
    return (a, b)

        

distro.register(
    name        = 'Left_Right_Triangular',  #special case of triangular where c==a
    domain      = distro.Domain.Continuous,
    params      = ('a','b'),  #assumes c==a
    paramSolver = _solver,
    cdf         = lambda x, a, b : 1 - ((b-x)/(b-a))**2,
    sample      = lambda a, b: triang.rvs(0,loc=a,scale=b-a),
    fittingFns  = {
        distro.Stat.Skew: lambda a, b : float(triang.stats(0,loc=a,scale=b-a,moments='s')),
        distro.Stat.Kurt: lambda a, b : float(triang.stats(0,loc=a,scale=b-a,moments='k')) + 3,
        distro.Stat.Min : lambda a, b : a, 
        distro.Stat.Min : lambda a, b : b
    }
)
