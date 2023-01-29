# Устройство состоит из трех деталей.
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

p1 = 0.1
p2 = 0.2
p3 = 0.25
q1 = 1 - p1
q2 = 1 - p2
q3 = 1 - p3

# Делал таблицу для самопроверки. Оставил как часть решения
pa0 = q1 * q2 * q3                                  # Что сломается ноль деталей. далее также
pa1 = p1 * p2 * q3 + p1 * q2 * p3 + q1 * p2 * p3
pa2 = p1 * q2 * q3 + q1 * p2 * q3 + q1 * q2 * p3
pa3 = p1 * p2 * p3
pa = pa0 + pa1 + pa2 + pa3

answer_a = pa3
answer_b = pa2
answer_c = (1 - pa0, pa1 + pa2 + pa3)
answer_d = pa1 + pa2

print('{:.3f}'.format(answer_a))
print('{:.3f}'.format(answer_b))
print((answer_c))                                   # не форматирует в tuple?
print('{:.3f}'.format(answer_d))
