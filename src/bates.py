import distro, math, numpy, random


def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    b0 = 2*mu
    n = round(b0**2/(12*sig2))
    b = math.sqrt(12*n*sig2)


distro.register(
    name        = 'Bates',
    domain      = distro.Domain.Continuous,
    params      = ('b','n'),  #to simplify guesses that paramater a==0
    paramSolver = _solver,
    cdf         = lambda x, b, n : 0, #not implemented
    sample      = lambda b , n : numpy.mean([random.random()*b for i in xrange(n)]), #assumes a=0
    fittingFns  = {
        distro.Stat.Skew: lambda b, n : 0,
        distro.Stat.Kurt: lambda b, n : -1.2/n+3,
    }
)


