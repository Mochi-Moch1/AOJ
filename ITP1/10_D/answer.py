import math
n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

for p in [1.0, 2.0, 3.0]:
    d = 0.0
    for xi, yi in zip(x, y):
        d += abs(xi - yi)**p
    d = d**(1.0/p)
    print(d)
d_inf = max([abs(xi-yi) for xi, yi in zip(x, y)])
print(d_inf)
