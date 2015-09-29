import scipy.stats as stats, distro, math

Normal = distro.Distribution(
    name   = 'Normal',
    domain = distro.Domain.Continuous,
    cdf    = lambda x, (mu, sig) : stats.norm.cdf(x, mu, sig),
    solver = lambda mean, var: (mean, math.sqrt(var)),
    params = ('mu', 'sigma')
)
print Normal