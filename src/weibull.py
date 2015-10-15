import distro, math, numpy 
from scipy.optimize import fsolve
from scipy.special import gamma

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2, distro.Stat.Skew])
    equations = lambda (lamb,k): (lamb*gamma(1+1.0/k)-mu , lamb**2*(gamma(1+2./k)-gamma(1+1./k)**2)-sig2)
    lamb, k = fsolve(equations,(1.0,1.0))
    return (lamb,k)

distro.register(
    name        = 'Weibull',
    domain      = distro.Domain.Continuous,
    params      = ('lamb','k'),
    paramSolver = _solver,
    cdf         = lambda x, lamb, k : (1-math.exp(-(x/lamb)**k) if x>=0 else 0),
    sample      = lambda lamb, k : numpy.random.weibull(k)*lamb,
    fittingFns  = {
        distro.Stat.Skew: lambda lamb, k : (2*gamma(1+1./k)**3-3*gamma(1+1./k)*gamma(1+2./k))/( gamma(1+2./k) - gamma(1+1./k)**2)**1.5    +  gamma(1+3./k)/( gamma(1+2./k) - gamma(1+1./k)**2)**1.5,
        distro.Stat.Kurt: lambda lamb, k : (-6*gamma(1+1./k)**4+12*gamma(1+1./k)**2*gamma(1+2./k)-3*TT**2-4*gamma(1+1./k)*gamma(1+3./k)+gamma(1+4./k)) / (gamma(1+2./k)-gamma(1+1./k)**2)**2 + 3,
        distro.Stat.Med:  lambda lamb, k: lamb*math.log(2.)**(1./k)
    }
)



