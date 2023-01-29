# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

p1 = 0.9
p2 = 0.8
p3 = 0.6

# P(B|A) = P(A|B) * P(B) / P(A), B - стрелок, A - попадание P(B|A) - вероятность что попал конкретный стрелок
# P(A) - общая вероятность попадания, P(A|B) - вероятность попадания конкретного стрелка

pa = p1 * (1/3) + p2 * (1/3) + p3 * (1/3)
pb_a1 = p1 * (1/3) / pa

print('{:.2f}'.format(pb_a1))

# Проверка себя формула Байеса используется когда другое событие уже произошло, значит сумма равна 1
# pb_a2 = p2 * (1/3) / pa
# pb_a3 = p3 * (1/3) / pa
# pol = pb_a1 + pb_a2 + pb_a3
# print('{:.2f}'.format(pol))