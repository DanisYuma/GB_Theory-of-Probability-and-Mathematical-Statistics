# Найти ско СВ Х, распределенной по биномиальному закону с параметрами n=50, p=0.6

p = 0.6
n = 50

q = 1 - p
sko = (n * p * q) ** 0.5
print('{:.2f}'.format(sko))