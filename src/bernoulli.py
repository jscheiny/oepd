import distro

def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    return (mu,)

bernoulli = distro.Distribution(
    name        = 'Bernoulli',
    domain      = distro.Domain.Discrete,
    params      = ('p', ),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    fittingFns  = {
        distro.Stat.Sig2: lambda p : p*(1-p),
        distro.Stat.Skew: lambda p : (1-2*p)/math.sqrt(p*(1-p)),
        distro.Stat.Kurt: lambda p : (1-6*p*(1-p))/(p*(1-p))+3
    }
)
