import math, numpy, utils



#PARAMS: k (shape), theta (scale)

def expected_value(k,theta):
	return k*theta

def variance(k,theta):
	return k*theta**2

def skewness(k,theta):
	return 2/math.sqrt(k)

def kurtosis(k,theta):
	return 6/k+3

def pdf(k,theta,x):
	1/(math.gamma(k)*theta**k)*x**(k-1)*math.exp(-x/theta)


def solver(mu,sig2):
	theta = float(sig2)/mu
	k = float(mu)/theta
	params = [k, theta]
	return params


def goodness_of_fit(mu,sig2,skew=None,kurt=None):
	#returns:
	#-1 if no fit
	#0  if trivial fit found (in this case if only mu and sig2 are given)
	#1  if decent fit
	#2  if good fit
	#3  if ggggg-great fit
	params = solver(mu,sig2)
	fitlist=[]	
	if skew!=None:
		fit = utils.approx_equal(skew,skewness(*params))
		fitlist.append(fit)
	if kurt!=None:
		fit = utils.approx_equal(kurt,kurtosis(*params))
		fitlist.append(fit)
	return utils.fits2score(fitlist)
