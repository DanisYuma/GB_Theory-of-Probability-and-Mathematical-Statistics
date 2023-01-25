# Квартили (quartile)
# k - квартиль. Первый 25%, третий 75%
# n - количество элементов
# if (n * k / 100) integer 

import numpy as np

x = np.array([1, 2, 4, 2, 1, 5, 7, 2, 3, 5, 7, 8, 9])
print(x)

print('{:.3f}'.format(np.std(x, ddof=1))) 

print('{:.3f}'.format(np.sqrt(np.var(x, ddof=1)))) 
