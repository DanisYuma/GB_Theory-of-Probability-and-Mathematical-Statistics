# Медиана
# Median

import numpy as np

z = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 65])
# z = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65])

z.sort()
n = len(z)
h = int(n / 2)

if n % 2 == 0:
    a = (z[h - 1] + z[h]) / 2
else:
    a = (z[h])

print(z)
print(n)
print(a)
