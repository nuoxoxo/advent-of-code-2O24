TEST=1
G = [list(_) for _ in open(0).read().splitlines()]
if TEST:
    for g in G:print(''.join(g))
R,C = len(G), len(G[0])
sr,sc,er,ec=None,None,None,None#S,E=None,None
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':sr,sc=r,c#S = (r,c)
        if G[r][c] == 'E':er,ec=r,c#E = (r,c)
D=((0,1),(1,0),(0,-1),(-1,0))
Q = [(0, 0, sr,sc, [])] # cost - heading - coor
SEEN = set([(0,sr,sc)])

def seepath(G,path,sr,sc):
    for i in range(len(G)):
        G[i] = [' ' if _ == '.' else _ for _ in G[i]]
        G[i] = ['@' if _ == '#' else _ for _ in G[i]]
    for r,c in path:G[r][c] = 'S' if r == sr and c == sc else '.'
    for g in G:print(' '.join(g))

import heapq#from collections import heapq
dist = None
T = []
while Q:
    cost,curr,r,c,path = heapq.heappop(Q)
    #print(cost,curr,coor, Q)
    if r == er and c == ec: 
        #print('reached/', r,c, cost)
        if not dist:
            dist = cost
            T += path + [(r,c)]
        elif dist == cost:
            T += path + [(r,c)]
        if TEST:
            print(path);seepath([_[:] for _ in G],path,sr,sc)
        #break # PART 1
    if (curr,r,c) not in SEEN:
        SEEN.add( (curr,r,c) )
    path = path + [(r,c)]
    dr,dc = D[curr]
    rr,cc = r + dr, c + dc
    #print('rr/cc', rr, cc)
    if -1<rr<R and -1<cc<C and G[rr][cc] != '#':
        heapq.heappush(Q, (cost + 1, curr, rr, cc, path))
    for t in (-1,1):
        newcurr = (curr + t) % 4
        if (newcurr,r,c) not in SEEN:
            heapq.heappush(Q, (cost + 1000, newcurr, r,c,path))
S = set()
for r,c in T:
    S.add((r,c))
if TEST: seepath([_[:] for _ in G],list(S),sr,sc)
print('part 1:', dist)
print('part 2:', len(S))
assert(dist in[88468,11048,7036]);
assert(len(S) in[45,64,616])
