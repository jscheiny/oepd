import distro, math, numpy 
from scipy.optimize import fsolve


def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2, distro.Stat.Skew])
    equations = lambda (alpha,beta): (alpha/(alpha+beta)-mu , alpha*beta/((alpha+beta)**2*(alpha+beta+1))-sig2)
    alpha, beta = fsolve(equations,(0.5,0.5))
    return (alpha,beta)

distro.register(
    name        = 'Beta',
    domain      = distro.Domain.Continuous,
    params      = ('alpha','beta'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda alpha, beta : numpy.random.beta(alpha,beta),
    fittingFns  = {
        distro.Stat.Skew: lambda alpha, beta : 2*(beta-alpha)*math.sqrt(alpha+beta+1)/(alpha+beta+2)/math.sqrt(alpha*beta),
        distro.Stat.Kurt: lambda alpha, beta : 6*( (alpha-beta)**2*(alpha+beta+1) - alpha*beta*(alpha+beta+2) ) / ( alpha*beta*(alpha+beta+2)*(alpha+beta+3) )
    }
)
