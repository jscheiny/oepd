import math, numpy, utils


def approx_equal(a,b,thresh=1e-6):
	return abs(a-b)<=thresh

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


def solver(mu,sig2,skew=-1,kurtosis=-1): #assumes that user knows inputs 1...k for some k, i.e. doesn't know mu and skew but not sig2
	theta = float(sig2)/mu
	k = float(mu)/theta
	params = [k, theta]
	if skew!=-1:
		if not approx_equal(skew,2/math.sqrt(k)):
			return False, []
	if kurtosis!=-1:
		if not approx_equal(kurtosis,6/k+3):
			return False, []
	return True, params
