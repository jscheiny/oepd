import math, numpy, utils



#PARAMS: lamb ("lambda" is a reserved word)

def expected_value(lamb):
	return 1.0/lamb

def variance(lamb):
	return 1.0/lamb**2

def skewness(lamb):
	return 2.0

def kurtosis(lamb):
	return 3.0

def pdf(lamb,x):
	lamb*math.exp(lamb*x)


def solver(mu):
	lamb = 1.0/mu
	return [lamb]

def goodness_of_fit(mu,sig2=None,skew=None,kurt=None):
	#returns:
	#-1 if no fit
	#0  if trivial fit found (in this case if only mu and sig2 are given)
	#1  if decent fit
	#2  if good fit
	#3  if ggggg-great fit
	params = solver(mu)
	fitlist=[]	
	if sig2!=None:
		fit = utils.approx_equal(sig2,variance(*params))
		fitlist.append(fit)
	if skew!=None:
		fit = utils.approx_equal(skew,skewness(*params))
		fitlist.append(fit)	
	if kurtosis!=None:
		fit = utils.approx_equal(kurt,kurtosis(*params))
		fitlist.append(fit)
	return utils.fits2score(fitlist)
