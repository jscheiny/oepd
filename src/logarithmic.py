import distro, math, numpy, utils
from scipy.optimize import fsolve


def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    equation = lambda p: -1/math.log(1-p)*p/(1.0-p)-mu
    p = fsolve(equation,.5)[0]
    return p

def _pmf(p,k):
    if k<1:
        return 0
    return -1/math.log(1-p)*p**k/float(k)

distro.register(
    name        = 'Logarithmic',
    domain      = distro.Domain.Discrete,
    params      = ('p',),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda p: utils.sample_naturals_from_pmf(lambda k: _pmf(p,k)),
    fittingFns  = {
        distro.Stat.Sig2: lambda p : -p*(p+math.log(1-p))/(1-p)**2/math.log(1-p)**2
    }
)
