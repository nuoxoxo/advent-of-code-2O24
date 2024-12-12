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
                sr, sc = Q.popleft()
                if g[sr][sc] != plant or (sr,sc) in SEEN:
                    continue
                SEEN.add((sr,sc))
                region.append((sr,sc))
                for dr,dc in D:
                    rr = sr + dr
                    cc = sc + dc
                    if -1<rr<R and -1<cc<C and (rr,cc) not in SEEN :
                        Q.append((rr,cc))
            # p1
            pmt=0
            fence=0
            for (sr,sc) in region:
                for dr,dc in D:
                    rr,cc = sr + dr, sc + dc
                    pmt += not (-1<rr<R and -1<cc<C) or g[rr][cc] != plant
            p1 += pmt * len(region)

            # p2
            noup, nodown, noleft, noright = set(),set(),set(),set()
            NU, ND, NL, NR = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)

            ### vertical
            for i,j in region:
                if i-1 < 0 or g[i-1][j] != plant: noup.add((i, j))
                if i+1 >= R or g[i+1][j] != plant: nodown.add((i, j))
            for i,j in noup: NU[i].append(j)
            for i,j in nodown: ND[i].append(j)

            ### horizontal
            for i,j in region:
                if j-1 < 0 or g[i][j-1] != plant: noleft.add((i, j))
                if j+1 >= C or g[i][j+1] != plant: noright.add((i, j))
            for i,j in noleft: NL[j].append(i)
            for i,j in noright: NR[j].append(i)

            ### count continuous fences
            def fencing(v) -> int:
                res = 1
                for i in range(len(v) - 1):
                    res += v[i] + 1 != v[i + 1]
                return res
            fence = sum([fencing(sorted(_)) for a in [NU,ND,NL,NR] for _ in a.values()])
            p2 += fence * len(region)

print('part 1:', p1);assert(p1 in [1456082,140,1930])
print('part 2:', p2);assert(p2 in [872382,  80,1206])
