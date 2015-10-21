import distro, math, numpy, utils, random
from scipy.optimize import fsolve
from scipy.special import gammainc
from scipy.special import gamma

def _solver(stats):
    (sig2, med) = distro.extractStats(stats, [distro.Stat.Sig2, distro.Stat.Med])
    Omega = med**2.
    equation  = lambda m :  Omega*(1-1./m*( gamma(m+0.5)/gamma(m) )**2)-sig2
    m = float(fsolve(equation,1.0))
    return (m,Omega)

def _cdf(x,m,Omega):
    return gammainc(m,m/float(Omega)*x**2)

distro.register(
    name        = 'Nakagami', 
    domain      = distro.Domain.Continuous,
    params      = ('m','Omega'),  #currently for accuracy need m>=11, but theoretically the bound is m>0.5
    paramSolver = _solver,
    cdf         = _cdf,
    sample      = lambda m, Omega: utils.solve_monotonic_increasing(lambda x: _cdf(x,m,Omega),random.random())
    fittingFns  = {
        distro.Stat.Mu: lambda m, Omega : gamma(m+0.5)/gamma(m)*(Omega/m)**0.5
    }
)


