import distro, math, numpy 


def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    return (mu*math.sqrt(math.pi/2),)

distro.register(
    name        = 'Half_Normal', #not to be confused with Jonah who is at best a quarter normal
    domain      = distro.Domain.Continuous,
    params      = ('tau',),
    paramSolver = _solver,
    cdf         = lambda x, tau : math.erf(x/(math.sqrt(2)*tau)),
    sample      = lambda tau: abs(numpy.random.normal(0,tau)),
    fittingFns  = {
        distro.Stat.Sig2: lambda tau : tau**2*(1-2/math.pi) #I think there might be a bug, double check with mathworld
    }
)


