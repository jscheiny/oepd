import distro, math, utils
from scipy.stats import rice
from scipy.optimize import fsolve

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    equations = lambda (nu, s) : ( float(rice.stats(nu,scale=s,moments='m'))-mu , float(rice.stats(nu,scale=s,moments='v'))-sig2 )
    (nu, s) = fsolve(equations, (10.0, 10.0))
    



    
distro.register(
    name        = 'Rice', #got rice bitch?
    domain      = distro.Domain.Continuous,
    params      = ('nu','s'), #s=scale
    paramSolver = _solver,
    cdf         = lambda x, nu, s : rice.cdf(x,nu,scale=s),
    sample      = lambda nu, s : rice.rvs(nu,scale=s),
    fittingFns  = {
        distro.Stat.Med: lambda nu, s : rice.median(nu,scale=s)
    }
)

    
