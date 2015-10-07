import distro, math, numpy 
from scipy.optimize import fsolve


def _solver(stats):
    (mu, sig2, skew) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2, distro.Stat.Skew])
    equations = lambda (n, a, b): (n*a/(a+b)-mu , n*a*b*(a+b+n)/(a+b)**2/(a+b+1)-sig2 , (a+b+2*n)*(b-a)/(a+b+2)*math.sqrt((1+a+b)/(n*a*b*(n+a+b)))-skew)
    n,a,b = fsolve(equations,(mu*2.0,1.0,1.0))
    return (round(n),a,b)

distro.register(
    name        = 'Beta_Binomial',
    domain      = distro.Domain.Discrete,
    params      = ('n','a','b'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda n, a, b : numpy.random.binomial(n,numpy.random.beta(a,b)),
    fittingFns  = {
        distro.Stat.Kurt: lambda n, a, b : (a+b)**2*(1+a+b)/( n*a*b*(a+b+2)*(a+b+3)*(a+b+n) ) * ( (a+b)*(a+b-1+6*n)+3*a*b*(n-2)+6*n**2-3*a*b*n*(6-n)/(a+b)-18*a*b*n**2/(a+b)**2 )
)
