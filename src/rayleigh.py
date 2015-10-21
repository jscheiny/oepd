import distro, math, numpy 


def _solver(stats):
    (mu,) = distro.extractStats(stats, [distro.Stat.Mu])
    tau = mu / math.sqrt(math.pi/2)
    return (tau,)

distro.register(
    name        = 'Rayleigh',
    domain      = distro.Domain.Continuous,
    params      = ('tau',),
    paramSolver = _solver,
    cdf         = lambda x, tau : 1-math.exp(-x**2/(2*tau**2)),
    sample      = lambda tau: numpy.random.rayleigh(tau),
    fittingFns  = {
        distro.Stat.Sig2: lambda tau : (4-math.pi)/2*tau**2,
        distro.Stat.Skew: lambda tau : 2*math.sqrt(math.pi)*(math.pi-3)/(4-math.pi)**1.5,
        distro.Stat.Kurt: lambda tau : -(6*math.pi**2-24*math.pi+16)/(4-math.pi)**2 + 3,
        distro.Stat.Med:  lambda tau : tau*math.sqrt(2*math.log(2))
    }
)


