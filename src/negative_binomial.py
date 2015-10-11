import distro, math, numpy 



def _solver(stats): #warning: this doesn't work well yet
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    p = 1-sig2/mu
    r = mu*(1-p)/p
    return (r,p)

distro.register(
    name        = 'Negative_Binomial',
    domain      = distro.Domain.Discrete,
    params      = ('r','p'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda N, K, n : numpy.random.negative_binomial(r,p),
    fittingFns  = {
        distro.Stat.Sig2: lambda r, p: (1+p)/math.sqrt(p*r),
        distro.Stat.Kurt: lambda r, p: 6.0/r + (1-p)**2/(p*r) + 3
	}
)
