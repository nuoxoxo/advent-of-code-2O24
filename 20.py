sr,sc,er,ec=None,None,None,None
G = [list(_) for _ in open(0).read().strip().splitlines()]
R,C=len(G),len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S': sr,sc=r,c
        if G[r][c] == 'E': er,ec=r,c
for g in G:print(' '.join(g).replace('.',' ').replace('#', '@'))
D=[(0,1),(1,0),(0,-1),(-1,0)]
import collections
Q = collections.deque([(sr,sc)])
DP = [[int(1e9)for _ in range(C)]for _ in range(R)]
DP[sr][sc] = 0
while Q:
    r,c = Q.popleft()
    for dr,dc in D:
        rr,cc = r + dr,c + dc
        if -1<rr<R and -1<cc<C and G[rr][cc] != '#':
            if DP[rr][cc] > DP[r][c] + 1:
                DP[rr][cc] = DP[r][c] + 1
                Q.append((rr,cc))
raw = DP[er][ec]
print('nocheat/84',raw)
res=0
s2,s4=0,0
for r in range(R):
    for c in range(C):
        # p1
        for dr in range(-2,3):
            for dc in range(-2,3):
                if abs(dr) + abs(dc) != 2:continue
                rr,cc = r + dr,c + dc
                if -1<rr<R and -1<cc<C and G[rr][cc]!='#':
                    if DP[rr][cc] - DP[r][c] == 2+2: s2 += 1
                    if DP[rr][cc] - DP[r][c] == 4+2: s4 += 1
                    if DP[rr][cc] - DP[r][c] >= 102: res += 1
print('res/',res)
print('sec2/14',s2)
print('sec4/14',s4)



