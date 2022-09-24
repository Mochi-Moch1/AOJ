import math
n = 1
while True:
    n = int(input())
    if n==0:
        break
    s = list(map(float, input().split()))
    ave = sum(s) / len(s)
    a2 = 0
    for i in s:
        a2 += (i - ave)**2
    a2 /= len(s)
    a = math.sqrt(a2)
    print(a)
