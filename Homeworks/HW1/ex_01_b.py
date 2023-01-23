# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from formula import combinations as c

m = (c(4, 48))
n = (c(4, 52))
q = m / n                   # Обратная ситуация, когда тузов нету
p = 1 - q

print('{:.3f}'.format(p))