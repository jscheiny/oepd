import math, numpy, utils



#PARAMS: a, b

def expected_value(a,b):
	return (a+b)/2.0

def variance(a,b):
	n = b-a+1
	return (n**2-1.0)/12

def skewness(a,b):
	return 0

def kurtosis(a,b):
	n = b-a+1.0	
	return -6*(n**2+1)/5./(n**2-1)

def pdf(a,b,x):
	n = b-a+1.0	
	if x not in range(a,b+1):
		return 0
	else:
		return 1.0/n


def solver(mu,sig2):
	roots = utils.solve_quadratic_eqn(1,-2*mu-1,mu**2+mu-3*sig2)
	if roots==None:
		return None
	else:
		a = min(roots)
		b = 2*mu-a
		return [a, b]

		


def goodness_of_fit(mu,sig2,skew=None,kurt=None):
	params = solver(mu,sig2)
	if params==None:
		return -1
	fitlist=[]	
	if skew!=None:
		fit = utils.approx_equal(skew,skewness(*params))
		fitlist.append(fit)
	if kurt!=None:
		fit = utils.approx_equal(kurt,kurtosis(*params))
		fitlist.append(fit)
	return utils.fits2score(fitlist)
