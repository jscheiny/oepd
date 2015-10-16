import distro, math, numpy 


def _solver(stats):
    (sig2,) = distro.extractStats(stats, [distro.Stat.Sig2])
    nu = 2/(1-1./sig2)
    return (nu,)

distro.register(
    name        = 'Students_t',
    domain      = distro.Domain.Continuous,
    params      = ('nu',),
    paramSolver = _solver,
    cdf         = lambda x, nu : 0, #unimplemented
    sample      = lambda nu : numpy.random.standard_t(nu),
    fittingFns  = {
        distro.Stat.Mu: lambda nu : 0,
        distro.Stat.Skew: lambda nu : 0,
        distro.Stat.Kurt:  lambda nu: 6/(nu-4.)+3,
        distro.Stat.Med: lambda nu : 0
    }
)



