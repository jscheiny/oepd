import distro
import bernoulli, binomial, exponential, gamma, geometric, normal, uniform_discrete

def main():
    uniformDiscrete = distro.find('Uniform Discrete')
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=0, kurt=-1.25)
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=0, kurt=-1.3)
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=.1, kurt=-1.3)

    matches = distro.matches(domain = distro.Domain.Discrete, mu=6.0, sig2=4.0, skew=.1, kurt=-1.3)
    for (fit, d, params) in matches:
        paramStr = ', '.join('%s=%g' % (k, v) for k, v in params.iteritems())
        print 'Fit=%d: %s where %s' % (fit, d.name, paramStr)


if __name__ == '__main__':
    main()
