f = open('countin.txt', 'r')
e = f.readline()
r = 1
w = open('countout.txt', 'w')
for r in range(int(e)):
    w.write(str(r + 1) + '\n')
    r + 1
