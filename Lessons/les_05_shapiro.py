import numpy as np
import scipy.stats as stats
import pylab
import matplotlib.pylab as plt

s = np.random.normal(0, 1, 50)

stats.shapiro(s)

stats.probplot(s, dist= "norm", plot= plt)
plt.show()
