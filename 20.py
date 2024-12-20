sr,sc,er,ec=None,None,None,None
G = [list(_) for _ in open(0).read().strip().splitlines()]
R,C=len(G),len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S': sr,sc=r,c
        if G[r][c] == 'E': er,ec=r,c
for g in G:print(''.join(g))
D=[(0,1),(1,0),(0,-1),(-1,0)]
import collections
def DP(G):
    Q = collections.deque([(sr,sc)])
    dp = [[int(1e9)for _ in range(C)]for _ in range(R)]
    dp[sr][sc] = 0
    while Q:
        r,c = Q.popleft()
        for dr,dc in D:
            rr,cc = r + dr,c + dc
            if -1<rr<R and -1<cc<C and G[rr][cc] != '#':
                if dp[rr][cc] > dp[r][c] + 1:
                    dp[rr][cc] = dp[r][c] + 1
                    Q.append((rr,cc))
    return dp[er][ec]
raw = DP(G)#[_[:] for _ in G])
print('nocheat/',raw)
res=0
s2=0
for r in range(R):
    for c in range(C):
        if G[r][c] != "#": continue
        G[r][c] = '.'
        test = DP(G)
        test = raw - test
        #if test > 0: print('test/',test)
        if test == 2: s2+=1
        if test >= 100:
            res+=1
        G[r][c] = '#'
print('res/',res)
print('2sec/',s2,'expect/',14)
