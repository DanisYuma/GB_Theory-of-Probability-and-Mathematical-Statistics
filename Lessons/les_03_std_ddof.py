# несмещенное стандартное отклонение (std) и дисперсия (var) + дельта степени свободы (ddof)
# standard deviation (std) and variance (var) + the Delta Degrees of Freedom (ddof)

import numpy as np

x = np.array([167, 181, 174, 178, 175, 164, 182, 178, 193, 166, 154, 170, 177])
print(x)

print('{:.3f}'.format(np.std(x, ddof=1))) 

print('{:.3f}'.format(np.sqrt(np.var(x, ddof=1)))) 
