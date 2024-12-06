g = open(0).read().splitlines()
sr,sc = None,None
R,C = len(g), len(g[0])
for r in range(R):
    for c in range(C):
        if g[r][c] == '^':
            sr,sc = r, c
            break
assert(sr != None and sc != None)

# part 2
def p2(g, rr: int, cc: int) -> bool:
    g[rr] = g[rr][:cc] + '#' + g[rr][cc + 1:]
    #if rr == 6 and cc == 3: for l in g:print('dbg/', l)
    r,c=sr,sc
    D = [ (-1,0), (0,1), (1,0), (0,-1) ]
    i = 0
    S = set([(sr,sc,i)])
    while 42:
        dr,dc = D[i]
        rr, cc = r + dr, c + dc
        if not (-1<rr<R and -1<cc<C):
            return False
        if g[rr][cc] == '#':
            i = (i + 1) % 4
        else:
            r,c = rr,cc
        if (rr,cc,i) in S:
            return True
        S.add((r,c,i))
    assert(False)

# part 1 and 2
r,c=sr,sc
SEEN = set([(sr,sc)])
D = [ (-1,0), (0,1), (1,0), (0,-1) ]
i = 0
while 42:
    dr,dc = D[i]
    rr, cc = r + dr, c + dc
    if not (-1<rr<R and -1<cc<C):
        #print('p1/end', len(SEEN))
        break
    if g[rr][cc] == '#':
        i = (i + 1) % 4
    else:
        r,c = rr,cc
        SEEN.add((r,c))

r2 = 0
for r, c in SEEN:
    r2 += p2(g[:],r,c)

print('part 1:', len(SEEN))
print('part 2:', r2)
