f = open('tripin.txt', 'r')
a = int(f.readline())
tri = []
for i in range(a):
    tri.append(f.readline())
    if (tri / 3 == 4):
         print tri
    else:
         print "nothing here!"
