# Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900

# 2 независимые выборки => Критерий Манна-Уитни
import numpy as np
import scipy.stats as stats

x1 = np.array([380,420, 290])
x2 = np.array([140, 360, 200, 900])

stats.mannwhitneyu(x1, x2)
print(stats.mannwhitneyu(x1, x2)) # Статистических различий нет так как pvalue=0.62 > 0.05

# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)