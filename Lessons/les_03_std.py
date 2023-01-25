# смещенное стандартное отклонение (std) и дисперсия (var)
# standard deviation (std) and variance (var)

import numpy as np

x = np.array([167, 181, 174, 178, 175, 164, 182, 178, 193, 166, 154, 170, 177])
print(x)

print('{:.3f}'.format(np.std(x))) 

print('{:.3f}'.format(np.sqrt(np.var(x)))) 
