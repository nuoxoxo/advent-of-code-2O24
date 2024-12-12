g = open(0).read().splitlines()
R,C = len(g),len(g[0])
D = ((-1,0),(0,1),(1,0),(0,-1))
SEEN = set()
res = 0
import collections
for r in range(R):
    for c in range(C):
        if (r,c) not in SEEN:
            plant = g[r][c]
            region = []
            Q = collections.deque()
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
                    #print(plant,'-', rr,cc,'-',region)
            print(plant, region)
            pmt=0
            for (sr,sc) in region:
                for dr,dc in D:
                    rr,cc = sr + dr, sc + dc
                    if not (-1<rr<R and -1<cc<C) or g[rr][cc] != plant:
                        pmt += 1
            print(plant, pmt)
            res += pmt * len(region)
print(res)

