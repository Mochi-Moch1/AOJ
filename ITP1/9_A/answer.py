W = input()
counter = 0
while True:
    T = input()
    if T == 'END_OF_TEXT':
        break
    T = T.split()

    t = []
    for s in T:
        t.append(s.lower())
    
    for s in t:
        if W == s:
            counter += 1
print(counter)