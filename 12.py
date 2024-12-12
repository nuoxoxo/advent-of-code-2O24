g = open(0).read().splitlines();
for l in g:print(l)
R,C = len(g),len(g[0])
D = ((-1,0),(0,1),(1,0),(0,-1))
SEEN = set()
res = 0
res2 = 0
from collections import defaultdict,deque
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
                    #print(plant,'-', rr,cc,'-',region)
            print('plant/', plant, '\nregion/', region)
            pmt=0
            fence=0
            for (sr,sc) in region:
                for dr,dc in D:
                    rr,cc = sr + dr, sc + dc
                    if not (-1<rr<R and -1<cc<C) or g[rr][cc] != plant:
                        pmt += 1
            #print('pmt/', plant, pmt)
            res += pmt * len(region)

            ### p2

            noup, nodown, noleft, noright = set(),set(),set(),set()
            UP,DO,LE,RI=defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list)
            ## vertical
            for i,j in region:
                if i-1 < 0 or g[i-1][j] != plant: noup.add((i, j))
                if i+1 >= R or g[i+1][j] != plant: nodown.add((i, j))
            print('noup/', sorted(list(noup)))
            print('nodown/', sorted(list(nodown)))
            for i,j in noup: UP[i].append(j)
            for i,j in nodown: DO[i].append(j)
            for k,v in UP.items():
                v=sorted(v)
                print('up/', k, v)
                fence += 1
                for i in range(len(v) - 1):
                    if v[i] + 1 != v[i + 1]: fence += 1
            print('fence/done up',fence)
            for k,v in DO.items():
                v=sorted(v)
                print('do/', k, v)
                fence += 1
                for i in range(len(v) - 1):
                    if v[i] + 1 != v[i + 1]: fence += 1
            print('fence/done down',fence)
            ### horizontal
            for i,j in region:
                if j-1 < 0 or g[i][j-1] != plant: noleft.add((i, j))
                if j+1 >= R or g[i][j+1] != plant: noright.add((i, j))
            print('noleft/', sorted(list(noleft)))
            print('noright/', sorted(list(noright)))
            for i,j in noleft: LE[j].append(i)
            for i,j in noright: RI[j].append(i)
            #for k,v in LE.items(): print('le/', k, v)
            for k,v in LE.items():
                v=sorted(v)
                print('left/', k, v)
                fence += 1
                for i in range(len(v) - 1):
                    if v[i] + 1 != v[i + 1]: fence += 1
            print('fence/done left',fence)
            #for k,v in RI.items(): print('ri/', k, v)
            for k,v in RI.items():
                v=sorted(v)
                print('right/', k, v)
                fence += 1
                for i in range(len(v) - 1):
                    if v[i] + 1 != v[i + 1]: fence += 1
            print('fence/done right',fence)
            res2 += fence * len(region);print()
            #print('fence/', plant, fence);print()
print(res)
print(res2)
