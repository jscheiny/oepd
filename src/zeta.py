import distro, math, numpy  
from scipy.optimize import fsolve
from scipy.special import zeta


Rzeta = lambda s: zeta(s,1.)

def _solver(stats): #warning: this doesn't work well yet
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    equation = lambda s: Rzeta(s-1)/Rzeta(s) - mu #only for s>2 (we need bounds)
    r = fsolve(equation,2.001)[0]
    return (r,)


distro.register(
    name        = 'Zeta',
    domain      = distro.Domain.Discrete,
    params      = ('s',),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda s : numpy.random.zipf(s),
    fittingFns  = {
        distro.Stat.Sig2: lambda s: (Rzeta(s)*Rzeta(s-2)-Rzeta(s-1)**2)/Rzeta(s)**2, #only if s>3 (we need bounds)
	}
)
