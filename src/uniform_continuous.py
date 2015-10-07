import distro, utils, random, math

def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    d = math.sqrt(3*sig2)
    a = mu-d
    b = mu+d
    return (a, b)



distro.register(
    name        = 'Uniform Continuous',
    domain      = distro.Domain.Continuous,
    params      = ('a', 'b'),
    paramSolver = _solver,
    cdf         = lambda x, a, b : (x-a)/(b-a),
    sample      = lambda a, b : random.random()*(b-a)+a,
    fittingFns  = {
        distro.Stat.Skew: lambda a, b : 0,
        distro.Stat.Kurt: lambda a, b : -1.2+3,
        distro.Stat.Med: lambda a, b : float(a+b)/2
    }
)
