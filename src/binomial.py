import distro, math, numpy

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    p = 1.0 - float(sig2)/mu
    n = mu/p
    return (n,p)

distro.register(
    name        = 'Binomial',
    domain      = distro.Domain.Discrete,
    params      = ('n','p'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda n, p : numpy.random.binomial(n,p),
    fittingFns  = {
        distro.Stat.Skew: lambda n, p : (1-2*p)/math.sqrt(n*p*(1-p)),
        distro.Stat.Kurt: lambda n, p : (1-6*p*(1-p))/math.sqrt(n*p*(1-p))+3
    }
)
