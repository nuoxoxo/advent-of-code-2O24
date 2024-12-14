lines = open(0).read().splitlines()
R,C=7,11
R,C=103,101
T = 100#6
coors = []
import collections
D=collections.defaultdict(int)
count=[0,0,0,0]#collections.defaultdict(int)
for line in lines:
    l,r = line.split()
    pl,pr = l[2:],r[2:]
    c,r = list(map(int, pl.split(',')))
    dc,dr = list(map(int, pr.split(',')))
    #print((r,c),(dr,dc))
    for _ in range(T):
        #print(r,c)
        rr,cc = r + dr, c + dc
        if rr < 0: rr = R + rr
        elif rr >= R:rr = rr - R
        if cc < 0: cc = C + cc
        elif cc >= C:cc = cc - C
        r,c = rr,cc
    D[(r,c)] += 1
for pos,val in D.items():
    print('d/', pos,val)
    r,c = pos
    if r<R//2 and c<C//2: count[0] += val
    if r<R//2 and c>C//2: count[1] += val
    if r>R//2 and c<C//2: count[2] += val
    if r>R//2 and c>C//2: count[3] += val
print(count)
res=1
for n in count:
    res*=n
print(res)
