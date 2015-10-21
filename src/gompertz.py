import distro, math, utils
from scipy.optimize import fsolve
from scipy.stats import gompertz

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    sig2overmu2 = lambda nu : float(gompertz.stats(nu,moments='v'))/float(gompertz.stats(nu,moments='m'))**2
    val = sig2/mu**2
    nu = utils.solve_monotonic_increasing(sig2overmu2,val,1.,100.)
    b = mu/float(gompertz.stats(nu,moments='m'))
    return (nu,b)

distro.register(
    name        = 'Gompertz',
    domain      = distro.Domain.Continuous,
    params      = ('nu','b'),  #this is no newbie distro though
    paramSolver = _solver,
    cdf         = lambda x, nu, b : gompertz.cdf(x,nu,scale=b)  #(1-math.exp(-nu*(math.exp(b*x)-1)) if x>=0 else 0),
    sample      = lambda nu, b : gompertz.rvs(nu,scale=b) ,
    fittingFns  = {
        distro.Stat.Skew: lambda nu, b : float(gompertz.stats(nu,moments='s')),
        distro.Stat.Kurt: lambda nu, b : float(gompertz.stats(nu,moments='k')) + 3,
        distro.Stat.Med : lambda nu, b : gompertz.median(nu,scale=b)
    }
)

    
