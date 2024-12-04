L = open(0).read().splitlines()
rev = [''.join(_) for _ in list(zip(*L))]
t = 'XMAS'
R, C = len(L), len(L[0])
r2,r1=0,0

# p2
def grid(G) -> bool:
    out = G[0][0] + G[0][-1] + G[-1][-1] + G[-1][0]
    return G[1][1] == 'A' and out in ['MSSM','SSMM','SMMS','MMSS']

for r in range(R - 2):
    for c in range(C - 2):
        sub = []
        for rr in range(r, r + 3):
            sub.append(L[rr][c:c + 3])

        if grid(sub):
            r2 += 1
# p1
D = [(1,1),(1,-1)]
def hove(s:str) -> int:
    res = 0
    for i in range(len(s) - 3):
        sub = s[i:i + 4]
        if sub == t or sub == t[::-1]:#Counter(sub) == Counter(t):
            res += 1
    return res

def diag(r:int, c:int) -> int: 
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
        if len(sub) == 4 and sub == t or sub == t[::-1]:
            res += 1
    return res

for l,r in zip(L, rev):
    r1 += hove(l) + hove(r)
for r in range(R):
    for c in range(C):
        r1 += diag(r,c)

print('part 1:', r1)
print('part 2:', r2)
