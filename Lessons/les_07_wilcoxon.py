# Критерий Уилкоксона 
# 
#  Исследуется влияние некоторой диеты на вес пациентов.  В исследовании участвуют 10 пациентов.

import numpy as np
import scipy.stats as stats

x1 = np.array([70, 74, 74.5, 79, 85, 93, 94, 98, 106.5, 107])
x2 = np.array([64, 76.5, 67, 73.5, 89, 85, 89.5, 91, 98, 100.5])
x3 = np.array([64, 76.5, 67, 73.5, 89, 85, 89.5, 91, 98, 113.5])

# x2 - x1

stats.wilcoxon(x1, x2)
print(stats.wilcoxon(x1, x2))       # Диета влияет так как pvalue=0.009 < 0.01

stats.wilcoxon(x1, x3)              # Диета не влияет так как pvalue=0.009 > 0.01
print(stats.wilcoxon(x1, x3))