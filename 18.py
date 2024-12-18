import re#, sys
N = 71
END = 1023
g = [['.'for _ in range( N )]for _ in range( N )]
D = [(0,1),(1,0),(0,-1),(-1,0)]
lines = open(0).read().strip().splitlines()

def printer(g,path):
    for r,c in path: g[r][c] = 'o'
    for gg in g:print(' '.join(gg))
    print()

def BFS(g):
    res = None
    Q = [(0,0,0,[(0,0)])]
    SEEN = set()
    ok = False
    while Q:
        node = Q.pop(0)
        r,c,cost,path = node
        if r == N - 1 and c == N - 1:
            res = node
            break
        if (r,c) in SEEN: continue
        SEEN.add((r,c))
        for dr, dc in D:
            rr,cc = r+dr,c+dc
            if -1<rr<N and -1<cc<N and g[rr][cc] != '#':
                Q.append((rr,cc,cost + 1,path + [(rr,cc)]))
    if not res: printer(g, path) # DBG/p2
    #printer(g, res[-1]) # DBG/p1
    return res

def checker(n,g):
    res = None
    for i,line in enumerate(lines):
        C,R = list(map(int,re.findall(r'\d+', line)))
        assert -1<C<N and -1<R<N
        g[R][C] = '#'
        if i == n:
            res = BFS(g)
            break
    return res

def p2() -> str:
    l,r = 0,len(lines)
    while l <= r:
        mid = (l + r) // 2
        res = checker(mid,[_[:] for _ in g])
        if res == None:
            r = mid - 1
        else:
            l = mid + 1
    return (l,lines[l])


part1 = checker(END,[_[:] for _ in g])[2]
part2 = p2()
print('part 1:', part1)
print('part 2:', part2[1])
assert part1 in [294,22]
assert part2[1] in ['31,22','6,1']


