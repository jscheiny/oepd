import distro, math, numpy  
from scipy.optimize import fsolve
from scipy.special import zeta


def H(n,m):
    return sum([1.0/k**m for k in range(n,0,-1)])


def _solver(stats): 
    (mu, maximum) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Max])
    equation = lambda s: H(maximum,s-1)/H(maximum,s)-mu
    s = fsolve(equation,2.0)[0]
    return (s,)



distro.register(
    name        = 'Zipf',
    domain      = distro.Domain.Discrete,
    params      = ('s',),
    paramSolver = _solver,
    cdf         = lambda s,k = 0, # unimplemented
    sample      = lambda s : 0, # unimplemented
    fittingFns  = {
        distro.Stat.Sig2: lambda s: 0, #unimplemented
	}
)
