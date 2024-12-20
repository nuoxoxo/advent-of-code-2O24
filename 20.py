sr,sc,er,ec=None,None,None,None
G = [list(_) for _ in open(0).read().strip().splitlines()]
R,C=len(G),len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S': sr,sc=r,c
        if G[r][c] == 'E': er,ec=r,c
for g in G:print(' '.join(g).replace('.',' ').replace('#', '@'))
D=[(0,1),(1,0),(0,-1),(-1,0)]
Q = [(sr,sc)]
DP = [[int(1e9)for _ in range(C)]for _ in range(R)]
DP[sr][sc] = 0
while Q:
    r,c = Q.pop(0)
    for dr,dc in D:
        rr,cc = r + dr,c + dc
        if -1<rr<R and -1<cc<C and G[rr][cc] != '#':
            if DP[rr][cc] > DP[r][c] + 1:
                DP[rr][cc] = DP[r][c] + 1
                Q.append((rr,cc))
raw = DP[er][ec]
print('nocheat/84',raw)
res,res2=0,0
s2,s4,s12=0,0,0
s50,s72=0,0
for r in range(R):
    for c in range(C):
        if G[r][c] == '#':continue
        bound = 2 # p1
        for dr in range(-bound,bound + 1):#(-2,3):
            for dc in range(-bound, bound + 1):#(-2,3):
                if abs(dr) + abs(dc) != bound: continue
                rr,cc = r + dr,c + dc
                if -1<rr<R and -1<cc<C and G[rr][cc] != '#':
                    if DP[rr][cc] - DP[r][c] == 2+bound: s2 += 1
                    if DP[rr][cc] - DP[r][c] == 4+bound: s4 += 1
                    if DP[rr][cc] - DP[r][c] == 12+bound: s12 += 1
                    if DP[rr][cc] - DP[r][c] >= 100+bound: res += 1
        B = 20 # p2
        for bound in range(B + 1):
            for dr in range(-bound,bound + 1):
                for dc in range(-bound, bound + 1):
                    if abs(dr) + abs(dc) != bound: continue
                    rr,cc = r + dr,c + dc
                    if -1<rr<R and -1<cc<C and G[rr][cc] != '#':
                        if DP[rr][cc] - DP[r][c] == 50+bound: s50 += 1
                        if DP[rr][cc] - DP[r][c] == 72+bound: s72 += 1
                        if DP[rr][cc] - DP[r][c] >= 100+bound: res2 += 1 # p2
print('res/',res)
print('sec2/14',s2);print('sec4/14',s4);print('sec12/3',s12);print()

print('res2/',res2)# 118801 124182 126896 lo
print('p2/sec50/32',s50);print('p2/sec72/22',s72)
assert res == 1378
assert res2 == 975379


