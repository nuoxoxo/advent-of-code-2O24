G = [list(_) for _ in open(0).read().splitlines()]
#for g in G:print(' '.join(g))
R,C = len(G), len(G[0])
S,E=None,None
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':S = (r,c)
        if G[r][c] == 'E':E = (r,c)
D=((0,1),(1,0),(0,-1),(-1,0))
Q = [(0, 0, S)] # cost - heading - coor
SEEN = set([(0,S)])
import heapq#from collections import heapq
heapq.heapify( Q )
"""(increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points)."""
while Q:
    cost,curr,coor = heapq.heappop(Q)
    r,c = coor
    #print(cost,curr,coor, Q)
    if coor == E: 
        print('reached/', coor, cost)
        break
    dr,dc = D[curr]
    rr,cc = r + dr, c + dc
    #print('rr/cc', rr, cc)
    if -1<rr<R and -1<cc<C and G[rr][cc] != '#' and (curr,(rr,cc)) not in SEEN:
        heapq.heappush(Q, (cost + 1, curr, (rr, cc)))
        SEEN.add((curr,(rr,cc)))
    for t in (-1,1):
        nc = (curr + t) % 4
        if (nc,coor) not in SEEN:
            heapq.heappush(Q, (cost + 1000, nc, coor))
            SEEN.add((nc,coor))
