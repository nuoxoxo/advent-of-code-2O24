g = open(0).read().splitlines();
R,C = len(g),len(g[0])
D = ((-1,0),(0,1),(1,0),(0,-1))
SEEN = set()
p1 = 0
p2 = 0
from collections import defaultdict, deque
for r in range(R):
    for c in range(C):
        if (r,c) not in SEEN:
            plant = g[r][c]
            region = []
            Q = deque()
            Q.append((r,c))
            while Q:
                i, j = Q.popleft()
                if g[i][j] != plant or (i,j) in SEEN:
                    continue
                SEEN.add((i,j))
                region.append((i,j))
                for dr,dc in D:
                    rr = i + dr
                    cc = j + dc
                    if -1<rr<R and -1<cc<C and (rr,cc) not in SEEN :
                        Q.append((rr,cc))
            # p1
            pmt=0
            for (i,j) in region:
                for dr,dc in D:
                    rr,cc = i + dr, j + dc
                    pmt += not (-1<rr<R and -1<cc<C) or g[rr][cc] != plant
            p1 += pmt * len(region)
            # p2
            fence=0
            NU, ND, NL, NR = defaultdict(list), \
                defaultdict(list), defaultdict(list), defaultdict(list)
            for i,j in region: # vertical
                if i-1 < 0 or g[i-1][j] != plant: NU[i].append(j)
                if i+1 >= R or g[i+1][j] != plant: ND[i].append(j)
                if j-1 < 0 or g[i][j-1] != plant: NL[j].append(i) # horizontal
                if j+1 >= C or g[i][j+1] != plant: NR[j].append(i)
            def fencing(v) -> int:
                return 1 + sum([v[i] + 1 != v[i + 1] for i in range(len(v) - 1)])
            for a in [NU,ND,NL,NR]:
                for _ in a.values():
                    fence += fencing(sorted(_))
            p2 += fence * len(region)
print('part 1:', p1);assert(p1 in [1456082,140,1930])
print('part 2:', p2);assert(p2 in [872382,  80,1206])
