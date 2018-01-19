f = open('encyin.txt', 'r')
line = f.readline().split()
n = int(line[0])
q = int(line[1])
pages = []
for i in range(n):
    pages.append(f.readline().strip())
w = open('encyout.txt', 'w')
for i in range(q):
    w.write(pages[int(f.readline().strip())-1] + '\n')
