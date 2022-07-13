x = int(46979)
h = int(x/3600)
x = x%3600
m = int(x / 60)
x = x % 60
s = x
print("{}:{}:{}".format(h, m, s))
