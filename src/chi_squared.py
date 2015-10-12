import distro, math, numpy 


def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    return (mu,)

distro.register(
    name        = 'Chi_Squared', 
    domain      = distro.Domain.Continuous,
    params      = ('k',),
    paramSolver = _solver,
    cdf         = lambda x, k : 0, #not implemented
    sample      = lambda k: abs(numpy.random.chisquare(k)),
    fittingFns  = {
        distro.Stat.Sig2: lambda k : 2*k,
        distro.Stat.Skew: lambda k : math.sqrt(8./k),
        distro.Stat.Kurt: lambda k : 12./k+3
    }
)


