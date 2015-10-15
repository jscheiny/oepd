import distro, math, numpy 
from scipy.optimize import fsolve
from scipy.special import gamma
from scipy.stats import invweibull

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    equations = lambda (alpha, s): (s*float(invweibull.stats(alpha,moments='m'))-mu , s**2*float(invweibull.stats(alpha,moments='v'))-sig2)
    s_approx = mu
    alpha_approx = 2*sqrt(4/sig2)
    alpha, s = fsolve(equations,(alpha_approx,s_approx))
    return (alpha,s)

distro.register(
    name        = 'Inverse_Weibull', #also called Frechet
    domain      = distro.Domain.Discrete,
    params      = ('alpha','s'),  #chose to set minimum param to m=0
    paramSolver = _solver,
    cdf         = lambda x, alpha, s : math.exp(-(x/s)**(-alpha)),
    sample      = lambda alpha, s : invweibull.rvs(alpha)*s ,
    fittingFns  = {
        distro.Stat.Skew: lambda alpha, s : invweibull.stats(alpha,moments='s'),
        distro.Stat.Kurt: lambda alpha, s : invweibull.stats(alpha,moments='k')+3,
        distro.Stat.Med : lambda alpha, s : s/(math.log(2))**(1/alpha)
    }
)


