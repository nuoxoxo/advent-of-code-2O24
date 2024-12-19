infile = open(0).read().splitlines()
R,C=7,11
R,C=103,101
T = 100#6
from collections import defaultdict

def printer(robs):
    G = [['.' for _ in range(C)] for _ in range(R)]
    for r,c,_,_ in robs: G[r][c] = '/'
    #for g in G:print(' '.join(g))
    for g in G[R//7*3:R//5*4]:print(' '.join(g[C//4:C//4*3]))

def newrc(r,c,dr,dc) -> (int, int):
    r = (r + dr + R) % R
    c = (c + dc + C) % C
    return (r,c)

def newrobot(line) -> (int,int,int,int):
    l,r = line.split()
    pl,pr = l[2:],r[2:]
    c,r = list(map(int, pl.split(',')))
    dc,dr = list(map(int, pr.split(',')))
    return (r,c,dr,dc)

def p2(lines) -> int:
    res = None
    robs = []
    for line in lines:
        robs.append( newrobot(line) )
    it = 1
    maxline = 0
    w,x,y,z=0,0,0,0
    for _ in range(10**4):#while 42:
        if it % 1000 == 0: print('@',it)
        for i,(r,c,dr,dc) in enumerate(robs):
            rr,cc = newrc (r,c,dr,dc)
            robs[i] = (rr,cc,dr,dc)
        changed = False # count max ine a line
        lens = defaultdict(int)
        for r,_,_,_ in robs: lens[r] += 1
        for v in lens.values():
            if v > maxline: maxline, changed = v, True
        if changed:
            if it == 7858:
                printer(robs)
                res = it
            print('----/', it) # change caused by maxline
        changed = False # try new way/ count in quadrants
        D = defaultdict(int)
        count=[0,0,0,0]
        for r,c,_,_ in robs:
            D[(r,c)] += 1
        for pos in D.keys():
            r,c = pos
            if r<R//2 and c<C//2-1: count[0] += 1
            if r<R//2 and c>C//2-1: count[1] += 1
            if r>R//2 and c<C//2-1: count[2] += 1
            if r>R//2 and c>C//2-1: count[3] += 1
        if w < count[0]: w, changed = count[0], True
        if x < count[1]: x, changed = count[1], True
        if y < count[2]: y, changed = count[2], True
        if z < count[3]: z, changed = count[3], True
        if changed:
            if it == 7858:
                res = it
                printer(robs)
            print('quad/', it)
        it += 1
    return res

def p1(lines) -> int:
    D = defaultdict(int)
    count=[0,0,0,0]#collections.defaultdict(int)
    for line in lines:
        r,c,dr,dc = newrobot(line)
        for _ in range(T):
            r,c = newrc(r,c,dr,dc)
        D[(r,c)] += 1
    for pos,val in D.items():
        r,c = pos
        if r<R//2 and c<C//2: count[0] += val
        if r<R//2 and c>C//2: count[1] += val
        if r>R//2 and c<C//2: count[2] += val
        if r>R//2 and c>C//2: count[3] += val
    res = 1
    for n in count:
        res*=n
    return res

res1, res2 = p1(infile), p2(infile)
print('part 1:', res1)
print('part 2:', res2)
assert(res1 in[12,221655456])
assert(res2 in[7858])
