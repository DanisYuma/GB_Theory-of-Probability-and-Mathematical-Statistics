# Пример: продавец утверждает, что он изготавливает детали размером 10 мм. Взята выборка из 12 деталей.
# Сигма генеральной совокупности неизвестна. 

import numpy as np
from scipy import stats
x0 = 10
x = np.array([10.50, 9.94, 10.42, 10.47, 10.4, 9.93, 9.17, 9.26, 10.11, 10.15, 10.5, 10.47])

mean = np.mean(x)
std = np.std(x, ddof=1)
length = len(x)
print(np.mean(x))
print(np.std(x, ddof=1))
print(len(x))

# z = x - u / d sqrt(len(x))
t = (mean - x0) / (std / np.sqrt(length))
print(t)

stats.ttest_1samp(x, 10)
print(stats.ttest_1samp(x, 10))

# Код и ошибки
# stats.ttest_ind(x, 10)
# RuntimeWarning: invalid value encountered in scalar multiply
#   var *= np.divide(n, n-ddof)  # to avoid error on division by zero

# Ttest_1sampResult(statistic = t, pvalue = mean)
# NameError: name 'Ttest_1sampResult' is not defined