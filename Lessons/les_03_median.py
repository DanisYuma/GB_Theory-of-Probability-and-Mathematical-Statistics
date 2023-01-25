# Медиана
# Median

import numpy as np

# z = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 65])
z = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65])

# z.shape
z.sort()
print(z)
n = len(z)
print(n)
h = int(n / 2)

if n % 2 == 0:
    a = (z[h] + z[h + 1]) / 2
else:
    a = (z[h + 1])

print('{:.3f}'.format(a))
