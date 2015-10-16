import distro, math
from scipy.optimize import fsolve
from scipy.stats import triang

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    equations = lambda (a, b): ( float(triang.stats(0.5,loc=a,scale=b-a,moments='m'))-mu , float(triang.stats(0.5,loc=a,scale=b-a,moments='v'))-sig2 )
    a , b = fsolve(equations, (mu-2.1*sig2,mu+2.1*sig2))
    return (a, b)

        

distro.register(
    name        = 'Isosceles_Triangular',  #special case of triangular where c==(a+b)/2
    domain      = distro.Domain.Continuous,
    params      = ('a','b'),  #assumes c==b
    paramSolver = _solver,
    cdf         = lambda x, a, b : (0.5*((x-a)/((a+b)/2.-a))**2 if x<(a+b)/2. else 1-0.5*((b-x)/(b-(a+b)/2.))**2),
    sample      = lambda a, b: triang.rvs(0.5,loc=a,scale=b-a),
    fittingFns  = {
        distro.Stat.Skew: lambda a, b : float(triang.stats(0.5,loc=a,scale=b-a,moments='s')),
        distro.Stat.Kurt: lambda a, b : float(triang.stats(0.5,loc=a,scale=b-a,moments='k')) + 3,
        distro.Stat.Min : lambda a, b : a, 
        distro.Stat.Min : lambda a, b : b,
        distro.Stat.Med : lambda a, b : (a+b)/2.
    }
)
