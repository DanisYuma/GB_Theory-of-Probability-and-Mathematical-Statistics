# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

import numpy as np

from math import factorial

def combinations (n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

p = 1 / (combinations(10, 3))

print('{:.5f}'.format(p))