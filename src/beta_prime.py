import distro, math
from scipy.stats import betaprime
from scipy.special import betainc

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    
    equation = lambda beta: sig2-float(betaprime.stats(mu*(beta-1),beta,moments='v'))
    beta = utils.solve_monotonic_increasing(equation,0,2.001,10000.,1e-6)
    alpha = (beta-1)*mu
    return (alpha,beta)



distro.register(
    name        = 'Beta_Prime',
    domain      = distro.Domain.Continuous,
    params      = ('alpha','beta'),
    paramSolver = _solver,
    cdf         = lambda x, alpha, beta : betainc(alpha,beta,x/(1.0+x)),
    sample      = lambda alpha, beta : betaprime.rvs(alpha,beta),
    fittingFns  = {
        distro.Stat.Skew: lambda alpha, beta : float(betaprime.stats(alpha,beta,moments='s'))
    }
)
