import distro, numpy, scipy

def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    rho = 1/(1-1.0/mu)
    return (rho,)

def _pmf(rho,k):
    if k<1:
        return 0
    return rho*scipy.special.beta(k,rho+1)  #test at home

distro.register(
    name        = 'Yule_Simon',
    domain      = distro.Domain.Discrete,
    params      = ('rho', ),
    paramSolver = _solver,
    cdf         = lambda rho, k : 1-k*scipy.special.beta(k,rho+1), # unimplemented
    sample      = lambda rho: utils.sample_naturals_from_pmf(lambda k: _pmf(rho,k)),
    fittingFns  = {
        distro.Stat.Sig2: lambda rho : rho**2/( (rho-1)**2 * (rho-2) ) ,
        distro.Stat.Skew: lambda rho : (rho+1)**2*math.sqrt(rho-2)/(rho-3)/rho, #if rho>2
        distro.Stat.Kurt: lambda rho : rho+3+(11*rho**3-49*rho-22)/( (rho-4)*(rho-3)*rho ) #if rho>4 (this doesn't seem right based on a sampling test, others check out)
    }
)
