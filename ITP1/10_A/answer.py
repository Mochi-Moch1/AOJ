import math
xy = list(map(float, input().split()))
x = (xy[0]-xy[2])**2
y = (xy[1]-xy[3])**2
distance = math.sqrt(x + y)
print(distance)
