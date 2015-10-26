import distro, math, numpy 
from scipy.optimize import fsolve
from scipy.stats import tukeylambda

def _solver(stats):
    (lo, hi, q1, q3, sig2) = distro.extractStats(stats, [distro.Stat.Min,distro.Stat.Max, Distro.Stat.Q1, Distro.Stat.Q3, distro.Stat.Sig2])
    if abs((q3-q1)/(hi-lo)-0.5)<.05:
        #lamb>=1
        equation = lambda lamb : sig2/hi**2 - lamb**2*tukeylambda.stats(lamb,scale=1,moments='v')
        lamb = utils.solve_monotonic_increasing(equation,0,1.,100.)
        s = hi*lamb
        return (lamb,s)
    else:
        #guess that s=1
        equation = lambda lamb : sig2-tukeylambda.stats(lamb,scale=1,moments='v')
        lamb = utils.solve_monotonic_increasing(equation,0,-0.4999,1)
        return (lamb,1)


distro.register(
    name        = 'Tukey_Lambda', #
    domain      = distro.Domain.Continuous,
    params      = ('lamb','s'),   #added scale param s
    paramSolver = _solver,
    cdf         = lambda x, lamb, s : tukeylambda.cdf(x,lamb, scale = s),
    sample      = lambda lamb, s : tukeylambda.rvs(lamb,scale=s),
    fittingFns  = {
        distro.Stat.Mu: lambda lamb, s : 0,
        distro.Stat.Skew: lambda lamb, s : 0,
        distro.Stat.Kurt : lambda lamb, s : float(tukeylambda.stats(lamb,scale=s,moments='k'))+3
    }
)


