from curses.ascii import isalpha
alphabets = {}
for i in range(97, 97+26):
    alphabets[chr(i)] = 0
while True:
    try:
        sentence = input().lower()
            
        for i in sentence:
            if i.isalpha():
                alphabets[i] += 1
    except EOFError:
        break

for alp, num in alphabets.items():
        print('{} : {}'.format(alp, num))