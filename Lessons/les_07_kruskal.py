# Крускала –Уоллиса  
# Критерий Крускала –Уоллиса 𝐻– непараметрический тест, используемый для сравнения нескольких групп.

# Чтобы рассчитать критерий Крускала-Уоллиса 𝐻 делаем следующее:
# Обобщим все данные в один ряд
# Присвоим ранги в этом ряду
# Посчитаем сумму рангов, присвоенных в общем ряду, но теперь уже в отдельных группах. Т.е. получим сумму рангов для каждой отдельной группы.
# Воспользуемся формулой:
# 𝐻=  12/(𝑁∗(𝑁+1) )∗∑1_(𝑖=1)^(𝑘_𝑗)▒〖𝑇_𝑗〗^2/𝑛_𝑗 −3(𝑁+1), 
# где N – общее число  измерений во всех сравниваемых выборках,
# 𝑘_𝑗- объем j-ой выборки 
# 𝑇_𝑗- сумма рангов в каждой выборке.

# Задача: Даны заработные платы людей, принадлежащих к трем разным профессиям (условия нормальности не соблюдается).
# 		gr 1: 70, 50, 64, 61, 75, 67, 73
# 		gr 2: 80, 78, 90, 68, 74, 65, 85
# 		gr 3: 141, 142, 140, 152, 161, 163, 155
#  
# Требуется определить, влияет ли профессия на заработную плату.

import numpy as np
import scipy.stats as stats

x1 = np.array([70, 50, 64, 61, 75, 67, 73])
x2 = np.array([80, 78, 90, 68, 74, 65, 85])
x3 = np.array([141, 142, 140, 152, 161, 163, 155])

stats.kruskal(x1, x2, x3)
print(stats.kruskal(x1, x2, x3))