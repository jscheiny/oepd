import distro, numpy, math
from scipy.optimize import fsolve


def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    equation = lambda rho: rho*math.exp(rho)/(math.exp(rho)-1)-mu
    rho = fsolve(equation,1.0)[0]
    return (rho)


def _cdf(rho):
    x = 0
    while x==0:
        x=numpy.random.poisson(rho)
    return x

distro.register(
    name        = 'Zero_Truncated_Poisson',
    domain      = distro.Domain.Discrete,
    params      = ('rho', ),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda rho : _cdf(rho), 
    fittingFns  = {
        distro.Stat.Sig2: lambda rho : rho*math.exp(rho)/(math.exp(rho)-1)*(1-rho/(math.exp(rho)-1))
    }
)
