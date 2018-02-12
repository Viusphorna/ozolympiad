f = open('dictin.txt', 'r')
l = f.readline().split()
d = int(l[0])
w = int(l[1])
trans = {}
for i in range(d):
    y = (f.readline().split())
    t = int(y[0])
    r = int(y[1])
    trans[t] = r
s = open('dictout.txt', 'w')
for k in range(w):
    q = (f.readline().split())
    h = int(q[0])
    if (h in trans):
        s.write(str(trans[h]) + '\n')
    else:
        s.write('C?' + '\n')
