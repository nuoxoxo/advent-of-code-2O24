import re#, sys
N = 71
g = [['.'for _ in range( N )]for _ in range( N )]
D = [(0,1),(1,0),(0,-1),(-1,0)]
p1,p2 = None, None
for i,line in enumerate(open(0).read().strip().splitlines()):
    C,R = list(map(int,re.findall(r'\d+', line)))
    assert -1<C<N and -1<R<N
    g[R][C] = '#'
    #if i == 1023:break
    Q = [(0,0,0)]
    SEEN = set()
    p2done = False
    while Q:
        tup = Q.pop(0)
        r,c,cost = tup
        if r == N - 1 and c == N - 1:
            if i == 1023: p1 = cost #'print('res/',cost, 'tpl/', tup)
            p2done = True
            break
        if (r,c) in SEEN: continue
        SEEN.add((r,c))
        for dr, dc in D:
            rr,cc = r+dr,c+dc
            if -1<rr<N and -1<cc<N and g[rr][cc] != '#':
                Q.append((rr,cc,cost + 1))
    if not p2done:
        p2 = str(C)+','+str(R)
        break #sys.exit()
print('part 1:', p1)
print('part 2:', p2)

