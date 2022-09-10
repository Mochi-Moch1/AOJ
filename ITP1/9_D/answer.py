s = input()
q = int(input())
command = []
for i in range(q):
    command = list(input().split())
    if command[0] == 'print':
        print(s[int(command[1]):int(command[2])])
    elif command[0] == 'reverse':
        tmp = s
        for i in range(int(command[1]), int(command[2])+1):
            for j in range(int(command[2]), int(command[1])-1):
                tmp[i], tmp[j] = tmp[j], tmp[i]
        s = tmp
    else:
        head = s[0:int(command[1])]
        tail = s[int(command[2]):-1]
        s = head + command[3] + tail
