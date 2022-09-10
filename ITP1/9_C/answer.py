n = int(input())

point_t = 0
point_h = 0
for i in range(n):
    taro, hanako = input().split()
    if taro < hanako:
        point_h += 3
    elif taro == hanako:
        point_t += 1
        point_h += 1
    else:
        point_t += 3

print(point_t, point_h)