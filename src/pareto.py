import distro, math, utils
from scipy.stats import pareto

def _solver(stats):
    (mu, sig2, lo) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2, distro.Stat.Min])
    equation = lambda alpha : (1-alpha/(alpha-1.))**2 / (alpha/((alpha-1)**2*(alpha-2)))  #(min-mu)**2/sig2 is a function only of alpha
    val = (lo-mu)**2/sig2
    alpha = utils.solve_monotonic_increasing(equation,val,2.01,100.)
    xm = (lo-mu)/(1-alpha/(alpha-1.))
    beta = lo - xm
    return (xm, alpha, beta)



    
distro.register(
    name        = 'Pareto',
    domain      = distro.Domain.Continuous,
    params      = ('xm','alpha','beta'), #added a location parameter, beta
    paramSolver = _solver,
    cdf         = lambda x, xm, alpha, beta : pareto.cdf(x,alpha,scale=xm, loc=beta),
    sample      = lambda xm, alpha, beta : pareto.rvs(alpha,scale=xm, loc=beta),
    fittingFns  = {
        distro.Stat.Med: lambda xm, alpha, beta : pareto.median(alpha,scale=xm,loc=beta) #higher moments seem inaccurate
    }
)

    
