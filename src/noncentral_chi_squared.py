import distro, math, numpy

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    lamb = sig2/2-mu
    k = mu-lamb
    return (k,lamb)

distro.register(
    name        = 'Noncentral_Chi_Squared',
    domain      = distro.Domain.Continuous,
    params      = ('k','lamb'),
    paramSolver = _solver,
    cdf         = lambda x, k, lamb : 0, # unimplemented
    sample      = lambda k, lamb: numpy.random.noncentral_chisquare(k,lamb),
    fittingFns  = {
        distro.Stat.Skew: lambda k, lamb : 2**1.5*(k+3*lamb)/(k+2*lamb)**1.5,
        distro.Stat.Kurt: lambda k, lamb : 12*(k+4*lamb)/(k+2*lamb)**2+3
    }
)
