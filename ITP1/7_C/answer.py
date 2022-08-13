r, c = map(int, input().split())


array = []
for i in range(r):
    array.append(list(map(int, input().split())))
    array[i].append(sum(array[i]))

total = [0] * (c+1)
for i in range(c+1):
    for j in range(r):
        total[i]+= array[j][i]

array.append(total)

for i in range(r+1):
    
    for j in range(c+1):
        if j == c:
            print(array[i][j])
        else:
            print(array[i][j], end=' ')
    