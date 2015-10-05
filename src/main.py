from uniform_discrete import *

def main():
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=0, kurt=-1.25)
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=0, kurt=-1.3)
    print uniformDiscrete.goodnessOfFit(mu=6, sig2=4, skew=.1, kurt=-1.3)

if __name__ == '__main__':
    main()
