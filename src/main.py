import distro, numpy, utils
import bernoulli, binomial, exponential, gamma, geometric, normal, uniform_discrete, uniform_continuous, erlang, poisson, borel, negative_binomial, half_normal, chi_squared, noncentral_chi_squared, fisher_snedecor, logistic, laplace, inverse_gaussian, bates, wigner_semicircle, raised_cosine, students_t, arcsine
import beta_binomial, hypergeometric, beta, yule_simon, zero_truncated_poisson, weibull, inverse_weibull, maxwell_boltzmann, reciprocal, left_right_triangular, right_right_triangular, isosceles_triangular #use scipy
#import zipf

def print_match_info(matches):
    print "********************"
    for (fit, d, params) in matches:
        paramStr = ', '.join('%s=%g' % (k, v) for k, v in params.iteritems())
        print 'Fit=%d: %s where %s' % (fit, d.name, paramStr)
    print "********************"


def main():
    uniformDiscrete = distro.find('Uniform Discrete')
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=0, kurt=-1.25)
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=0, kurt=-1.3)
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=.1, kurt=-1.3)

    matches = distro.matches(domain = distro.Domain.Discrete, mu=6.0, sig2=4.0, skew=.1, kurt=-1.3)
    print_match_info(matches)

    matches = distro.matches(domain = distro.Domain.Discrete, mu=6.0, sig2=4.0) #should give several trivial fits
    print_match_info(matches)
    
    matches = distro.matches(domain = distro.Domain.Continuous, mu=6.0, sig2=4.0) #should give several trivial fits
    print_match_info(matches)


    gamma = distro.find('Gamma')
    npts = 10**4
    data = [gamma.sample(3,5) for i in range(npts)]
    sample_mean = numpy.mean(data)
    sample_variance = utils.sampleVariance(data)
    sample_skewness = utils.sampleSkewness(data)
    sample_kurtosis = utils.sampleKurtosis(data)
    matches = distro.matches(domain = distro.Domain.Continuous, mu=sample_mean, sig2=sample_variance,skew=sample_skewness,kurt=sample_kurtosis)
    print_match_info(matches)  #should give decent or good fit for gamma(3,5)

    betabinomial=distro.find('Beta_Binomial')
    npts = 10**4
    data = [betabinomial.sample(50,1,2) for i in range(npts)]
    sample_mean = numpy.mean(data)
    sample_variance = utils.sampleVariance(data)
    sample_skewness = utils.sampleSkewness(data)
    sample_kurtosis = utils.sampleKurtosis(data)
    matches = distro.matches(domain = distro.Domain.Discrete, mu=sample_mean, sig2=sample_variance,skew=sample_skewness,kurt=sample_kurtosis)
    print_match_info(matches)  #should give decent or good fit for beta_binomial(50,1,2)



if __name__ == '__main__':
    main()
