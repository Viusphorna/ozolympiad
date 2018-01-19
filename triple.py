f = open('tripin.txt', 'r')
a = int(f.readline())
tri = []
for i in range(a):
     u = int(f.readline())
     if (u % 3 == 0):
        tri.append(i+1)
w = open('tripout.txt', 'w')
if (len(tri) != 0):
    w.write(str(len(tri)) + '\n')
    for r in tri:
        w.write(str(r) + ' ')
else:
    w.write("Nothing here!")
