import distro, math, numpy 



def _solver(stats):
    (mu, sig2) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2])
    d2 = round(2/(1-1.0/mu))
    d1 = round(2*d2**2*(d2-2) / (sig2*(d2-2)**2*(d2-4) - 2*d2**2))
    return (d1, d2)


distro.register(
    name        = 'Fisher_Snedecor', #often called F distribution
    domain      = distro.Domain.Continuous,
    params      = ('d1','d2'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda d1, d2 : (numpy.random.chisquare(d1)/d1) / (numpy.random.chisquare(d2)/d2),
    fittingFns  = {
        distro.Stat.Skew: lambda d1, d2 : (2*d1+d2-2)*math.sqrt(8*(d2-4))/( (d2-6)*math.sqrt(d1*(d1+d2-2)) ),
        distro.Stat.Kurt: lambda d1, d2 : 12 * ( d1*(5*d2-22)*(d1+d2-2) + (d2-4)*(d2-2)**2 ) / ( d1*(d2-6)*(d2-8)*(d1+d2-2) ) + 3
    }
)
