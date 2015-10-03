import math, numpy

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
