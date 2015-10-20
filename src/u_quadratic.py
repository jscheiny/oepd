import distro, math, utils, random


def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    b = (2*mu+math.sqrt(20.*sig2/3.))/2
    a = 2*mu-b
    return (a,b)

def _cdf(x,a,b):
    if x<a:
        return 0
    if x>b:
        return 1
    alpha = 12./(b-a)**3
    beta = (a+b)/2.
    return alpha/3*((x-beta)**3+(beta-a)**3)


distro.register(
    name        = 'U_Quadratic', 
    domain      = distro.Domain.Continuous,
    params      = ('a','b'),
    paramSolver = _solver,
    cdf         = _cdf,
    sample      = lambda a, b: utils.solve_monotonic_increasing(lambda x: _cdf(x,a,b),random.random(),a,b),
    fittingFns  = {
        distro.Stat.Skew: lambda a, b : 0,
        distro.Stat.Kurt: lambda a, b : 1.191  # based on experimentation, wiki gives 3./112*(b-a)**4, this seems wrong
        distro.Stat.Min : lambda a, b : a,
        distro.Stat.Min : lambda a, b : b
    }
)


