import re, sys
N = 71
g = [['.'for _ in range( N )]for _ in range( N )]
#for gg in g:print(''.join(gg))
D = [(0,1),(1,0),(0,-1),(-1,0)]
for i,line in enumerate(open(0).read().strip().splitlines()):
    c,r = list(map(int,re.findall(r'\d+', line)))
    #print(c,r)
    assert -1<c<N and -1<r<N
    g[r][c] = '#'
    #if i == 1023:break
Q = [(0,0,0)]
SEEN = set()
p2done = False
while Q:
    tup = Q.pop(0)
    r,c,cost = tup
    if r == N - 1 and c == N - 1:
        print(tup, '\nres/',cost)
        p2done = True
        break
    if (r,c) in SEEN: continue
    SEEN.add((r,c))
    for dr, dc in D:
        rr,cc = r+dr,c+dc
        if -1<rr<N and -1<cc<N and g[rr][cc] != '#':
            Q.append((rr,cc,cost + 1))
print(p2done)
if not p2done:
    print(r,c)
    sys.exit()
