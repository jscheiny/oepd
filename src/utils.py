import math, numpy, random

def nintegral(f,a,b,delta):
    xvals = numpy.arange(a,b,delta)
    yvals = [f(x) for x in xvals]
    return numpy.trapz(yvals,dx=delta)

def L2distance(f,g,a=0,b=1000):
    d = lambda x: (f(x)-g(x))**2
    l2squared = nintegral(d,a,b,0.01)
    return math.sqrt(l2squared)

def solve_quadratic_eqn(a,b,c):
    disc = b**2-4*a*c
    if disc<0:
        return None
    else:
        return (-b-math.sqrt(disc))/(2*a), (-b+math.sqrt(disc))/(2*a)


def sampleVariance(L):
    n = float(len(L))
    return numpy.var(L)*n/(n-1)

def sampleSkewness(L):
    mu = numpy.mean(L)
    sig = numpy.std(L)
    n = float(len(L))
    m3 = 1.0/n * sum([(x-mu)**3 for x in L])
    s3 = sampleVariance(L)**(1.5)
    return m3/s3

def sampleKurtosis(L):
    mu = numpy.mean(L)
    sig = numpy.std(L)
    n = float(len(L))
    m4 = 1.0/n * sum([(x-mu)**4 for x in L])
    m22 = sampleVariance(L)
    return m4/m22**2
    

def sample_naturals_from_pmf(pmffun):
    s=0
    r=random.random()
    i=-1
    while s<r:
        i+=1
        s+=pmffun(i)
    return i



    

