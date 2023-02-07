# Было проведено исследование научных статей на количество авторов в разные годы.
# Построить 90% и 95% интервалы
# Х ̅±𝑍_(𝛼/2)∗𝜎/√𝑛   

import math

z95 = 1.96     # из таблицы
z90 = 1.645

# 1946 n = 151, x = 2, s = 1.4
x = 2
s = 1.4
n = 151
ci1 = (x - (z95 * s / math.sqrt(n)), x + (z95 * s / math.sqrt(n)))
ci2 = (x - (z90 * s / math.sqrt(n)), x + (z90 * s / math.sqrt(n)))
print(ci1, ci2)

# 1956 n = 149, x = 2.3, s = 1.6
x = 2.3
s = 1.6
n = 149
ci1 = (x - (z95 * s / math.sqrt(n)), x + (z95 * s / math.sqrt(n)))
ci2 = (x - (z90 * s / math.sqrt(n)), x + (z90 * s / math.sqrt(n)))
print(ci1, ci2)
