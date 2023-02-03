import numpy as np
# import pylab
import scipy.stats as stats

s = np.random.normal(0, 1, 50)

stats.shapiro(s)