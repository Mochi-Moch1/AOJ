s = input()
p = input()

flag = False
for i in range(len(p)):
    if p in s:
        flag = True
        break
    else:
        s = s[1:]+s[0]
    

if(flag):
    print('Yes')
else:
    print('No')