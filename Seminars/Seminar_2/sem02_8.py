# Вероятность рождения мальчиков 0.515. Найти наивероятнейшее число девочек из 600 новорожденных.

n = 600
# n = 999 для проверки формулы
q = 0.515
p = 1 - q

if (n * p + p) % 1 == 0: 
    k0 = (n * p - q, n * p + p)
else:
    k0 = n * p // 1

print(k0)