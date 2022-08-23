sentense = input()
result = ''
for s in sentense:
    if s.islower():
        result += s.upper()
    elif s.isupper():
        result += s.lower()
    else:
        result += s
print(result)