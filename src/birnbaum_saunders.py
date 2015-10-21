import distro, math, numpy 
from scipy.stats import fatiguelife


#figure it out: mu = (1+shape**2/2.)*scale+loc, code it up later


def _solver(stats):
    (mu, med,lo) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Med, distro.Stat.Min])
    beta = lo
    s = med - beta
    alpha = sqrt((mu-lo)/s*2-1)
    return (alpha,beta,s)

distro.register(
    name        = 'Birnbaum_Saunders',
    domain      = distro.Domain.Continuous,
    params      = ('alpha','beta','s'), #alpha=shape, beta=loc, s=scale
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda alpha, beta, s : fatiguelife.rvs(alpha,loc=beta,scale=s),
    fittingFns  = {
        distro.Stat.Sig2: lambda alpha, beta, s  : float(fatiguelife.stats(alpha,loc=beta,scale=s,moments='v')) #all higher moments seem unreliable
    }
)
