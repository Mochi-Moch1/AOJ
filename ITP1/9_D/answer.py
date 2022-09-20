s = input()
q = int(input())
command = []
for i in range(q):
    command = list(input().split())
    if command[0] == 'print':
        print(s[int(command[1]):int(command[2])+1])
    elif command[0] == 'reverse':
        a = int(command[1])
        b = int(command[2]) + 1
        s = s[:a] + s[a:b][::-1] + s[b:]
    else:
        a = int(command[1])
        b = int(command[2]) + 1
        s = s[:a] + command[3] + s[b:]
