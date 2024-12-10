G = open(0).read().splitlines()
for g in G:print(g)
DIR = ((-1,0),(0,1),(1,0),(0,-1))
#p1,p2 = 0, 0
R, C = len(G), len(G[0])
from collections import defaultdict
def solve(part2):
    p1,p2 = 0, 0
    for r, row in enumerate(G):
        for c, dg in enumerate(row):
            if dg != '0': continue
            SEEN = set([(r,c)])
            Q = [(r,c)]
            tmp = 0
            if part2: D = defaultdict(int); D[(r,c)] = 1 # p2
            while Q:
                sr, sc = Q.pop(0)
                prev = int(G[sr][sc])
                if int(G[sr][sc]) == 9:
                    if part2: p2 += D[(sr,sc)] # p2
                    tmp += 1
                for dr, dc in DIR:
                    rr, cc = sr + dr, sc + dc
                    if rr in range(R) and cc in range(C) and int(G[rr][cc])==prev+1:
                        if (rr,cc) not in SEEN:
                            Q.append((rr,cc))
                            SEEN.add((rr,cc))
                        if part2: D[(rr,cc)] += D[(sr,sc)] # p2
            p1 += tmp
    assert(p1 % 100 in [36,9])
    if part2:
        assert(p2 % 100 in [26,9**2])
        return p2
    return p1

print('part 1:', solve(False));
print('part 2:', solve(True));
