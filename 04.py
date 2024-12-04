L = open(0).read().splitlines()
rev = [''.join(_) for _ in list(zip(*L))]
R, C = len(L), len(L[0])
t = 'XMAS'
r2,r1=0,0

# p1
def diag(r:int, c:int) -> int: 
    D = [(1,1),(1,-1)]
    res = 0
    for dr, dc in D:
        rr = r
        cc = c
        sub = L[r][c]
        for _ in range(3):
            rr += dr
            cc += dc
            if not (-1<rr<R and -1<cc<C):
                break
            sub += L[rr][cc]
        res += sub == t or sub == t[::-1]
    return res

for l,r in zip(L, rev):
    r1 += l.count(t) + l.count(t[::-1]) + r.count(t) + r.count(t[::-1])
for r in range(R):
    for c in range(C):
        r1 += diag(r,c)

# p2
def p2(g) -> bool:
    if g[1][1] != 'A':
        return False
    s = g[0][0] + g[0][-1] + g[-1][-1] + g[-1][0]
    return s.count('S') == 2 and s.count('M') == 2 \
        and ('SS' in s or 'MM' in s)

for r in range(R - 2):
    for c in range(C - 2):
        a = []
        for rr in range(r, r + 3):
            a.append(L[rr][c:c + 3])
        r2 += p2(a)

print('part 1:', r1)
print('part 2:', r2)
