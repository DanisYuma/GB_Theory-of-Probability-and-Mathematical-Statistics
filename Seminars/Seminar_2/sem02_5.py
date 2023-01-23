n = 25
p = 0.5
q = 1 - p

if (n * p + p) % 1 == 0: 
    k0 = (n * p - q, n * p + p)
else:
    k0 = n * p // 1
print(k0)