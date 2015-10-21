import distro, math, numpy 
from scipy.optimize import fsolve
from scipy.stats import genpareto

def _solver(stats): #tots doesn't work. i'll come back to it
    (mu, sig2,med) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2, distro.Stat.Med])
    equations = lambda (m, s, xi) : ( float(genpareto.stats(xi,loc=m,scale=s,moments='m'))/mu-1, float(genpareto.stats(xi,loc=m,scale=s,moments='v'))/sig2-1 , (m+s*(2**xi-1)/xi) / med-1 )
    (m, s, xi) = fsolve(equations,(10.,10.,.1))
    return (m,s,xi)




distro.register(
    name        = 'Generalized_Pareto', 
    domain      = distro.Domain.Continuous,
    params      = ('m','s','xi'),  #wiki uses mu, sigma and xi
    paramSolver = _solver,
    cdf         = lambda x, m, s, xi : 1-(1+xi*(x-m)/s)**(-1/xi),
    sample      = lambda alpha, s : genpareto.rvs(xi,loc=m,scale=s),
    fittingFns  = { #skewness is crap
    }
)


