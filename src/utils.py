import math, numpy

def nintegral(f,a,b,delta):
    xvals = numpy.arange(a,b,delta)
    yvals = [f(x) for x in xvals]
    return numpy.trapz(yvals,dx=delta)

def L2distance(f,g,a=0,b=1000):
    d = lambda x: (f(x)-g(x))**2
    l2squared = nintegral(d,a,b,0.01)
    return math.sqrt(l2squared)

def fits2score(fitlist):
    #given a list if fits as returned from approx_equal returns an overall score from -1 to 3 corresponding to:
    #-1 if no fit
    #0  if trivial fit found (in this case if only mu and sig2 are given)
    #1  if decent fit
    #2  if good fit
    #3  if ggggg-great fit
    if len(fitlist)==0:
        return 0
    if max(fitlist)>3:
        return -1
    if max(fitlist)==3:
        return 1
    if max(fitlist)==2:
        if len(fitlist)>2:
            return 3
        else:
            return 2    
    return 3

def approx_equal(a,b): #returns 1-5 (1-great fit, 2-good, ... 5-bad)
    if a<b:
        a,b = b,a
    if a<1e-5:
        err = 100*(b-a)
    else:
        err = 1.0*a/b-1
    if err<0.01:
        return 1
    if err<0.1:
        return 2
    if err<0.5:
        return 3
    if err<1:
        return 4
    return 5

def solve_quadratic_eqn(a,b,c):
    disc = b**2-4*a*c
    if disc<0:
        return None
    else:
        return (-b-math.sqrt(disc))/(2*a), (-b+math.sqrt(disc))/(2*a)
