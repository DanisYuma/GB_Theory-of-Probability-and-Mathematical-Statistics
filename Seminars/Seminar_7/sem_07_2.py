# При исследовании препарата для снижения кровяного давления у больных 3 раза измерялся сердечный выброс.
# Менялся ли сердечный выброс?
# Найти критерий вручную, проверьте значение функцией и интерпретируйте результат с использованием p-value

import numpy as np
import scipy.stats as stats

a = np.array([3.5, 3.3, 4.9, 3.6])
b = np.array([8.6, 5.4, 8.8, 5.6])
c = np.array([5.1, 8.6, 7.7, 5.0])

stats.friedmanchisquare(a, b, c)
print(stats.friedmanchisquare(a, b, c))     # Есть различия так как pvalue=0.03
# FriedmanchisquareResult(statistic=6.5, pvalue=0.03877420783172202)