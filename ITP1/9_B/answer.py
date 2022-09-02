while True:
    deck = input()
    if deck == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        tmp = []
        if h == 1:
            tmp = deck[0]
        else:
            tmp = deck[0:h]
        deck = deck[h:]
        deck = deck + tmp
    print(deck)
