import distro, math, numpy 
from scipy.optimize import fsolve


def sumTup2(tup):
    return sum([x^2 for x in tup])

def collapseTup(tup3):
    return (tup3[0]**2+0.5*tup3[1]**2,0.5*tup3[1]**2+tup3[1]**2)

def _solver(stats): #warning: this doesn't work well yet
    (mu, sig2, skew) = distro.extractStats(stats, [distro.Stat.Mu, distro.Stat.Sig2, distro.Stat.Skew])
    equations = lambda (N,K,n): (n*K/N-mu,
                                 n*K/N*(N-K)/N*(N-n)/(N-1) - sig2,
                                 (N-2*K)*(N-1)**0.5*(N-2*n)/(n*K*(N-K)*(N-n))**0.5/(N-2) - skew)
    Napprox,Kapprox,napprox = fsolve(equations,(mu*6.0,mu*4.0,mu*2.0))
    besterr = sumTup2(equations((round(Napprox),round(Kapprox),round(napprox))))*2
    print (round(Napprox),round(Kapprox),round(napprox)), besterr
    for N in range(int(Napprox/2),int(Napprox*2)+1):
        reduced_equations = lambda (K,n) : collapseTup(equations((N,K,n)))
        K, n = fsolve(reduced_equations,(Kapprox,napprox))
        K = round(K)
        n = round(n)
        err = sumTup2(equations((N,K,n)))
        print N, K, n, err
        if err<besterr:
            besterr=err
            besttup = (N,K,n)
    return besttup

distro.register(
    name        = 'Hypergeometric',
    domain      = distro.Domain.Discrete,
    params      = ('N','K','n'),
    paramSolver = _solver,
    cdf         = lambda x : 0, # unimplemented
    sample      = lambda N, K, n : numpy.random.hypergeometric(K,N-K,n),
    fittingFns  = {
        distro.Stat.Kurt: lambda N, K, n : 1/(n*K*(N-K)*(N-n)*(N-2)*(N-3)) * ( (N-1)*N**2*(N*(N+1)-6*K*(N-K)-6*n*(N-n))+6*n*K*(N-K)*(N-n)*(5*N-6))+3 #did one test to confirm this :)
)
