import pylab
import scipy.stats as stats

stats.probplot(s, dist= "norm", plot= pylab)
pylab.show()