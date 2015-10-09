import distro, math, numpy, random

def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    kappa = 1-1.0/mu
    return (kappa,)

def _pmf(kappa,n):
    if n<1:
        return 0
    return math.exp(-kappa*n)*(kappa*n)**(n-1)/math.factorial(n)

def _sampler(kappa):
    if kappa>0.85:
        raise ValueError("kappa must be <=0.85, can't handle large factorials")
    s=0
    r=random.random()
    i=0
    while s<r:
        i+=1
        if i==144:  #can't handle factorial greater than 140ish
            return i
        s+=_pmf(kappa,i)
    return i
         

distro.register(
    name        = 'Borel',
    domain      = distro.Domain.Discrete,
    params      = ('kappa',),  #wikipedia uses mu as the parameter, but this is confusing as the mean is also denoted mu and for this distro they are not equal (lame o'clock)
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = _sampler, # unimplemented
    fittingFns  = {
        distro.Stat.Sig2: lambda kappa : kappa/(1.0-kappa)**3,
    }
)
