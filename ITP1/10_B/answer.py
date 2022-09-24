import math
a, b, c = map(float, input().split())
C = math.radians(c)

area = 1/2 * a * b * math.sin(C)

d = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
circ = a + b + d

height = b * math.sin(C)

print(area)
print(circ)
print(height)