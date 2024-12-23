lines = open(0).read().splitlines()

NUMS = [
    ['7','8','9'],['4','5','6'],['1','2','3'],
    [None,'0','A'],
]

DIRS = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]
btns = '<^>vA'

def getn(r,c):
    if -1<r<4 and -1<c<3:
        return NUMS[r][c]
    return None

def getdir(r,c):
    if -1<r<2 and -1<c<3:
        return DIRS[r][c]
    return None

def nextn(r,c,btn):
    if btn == 'A': return (r,c,getn(r,c))
    if btn == '^': return (r-1,c,None)
    if btn == 'v': return (r+1,c,None)
    if btn == '<': return (r,c-1,None)
    if btn == '>': return (r,c+1,None)
    assert False

def nextdir(r,c,btn):
    if btn == 'A': return (r,c,getdir(r,c))
    if btn == '^': return (r-1,c,None)
    if btn == 'v': return (r+1,c,None)
    if btn == '<': return (r,c-1,None)
    if btn == '>': return (r,c+1,None)
    assert False

"""numeric keypad, its robotic arm is pointed 
at the A button in the bottom right corner""" # 3,2
"""directional keypad, its robot arm is pointed 
at the A button in the upper right corner""" # 0,2
res1 = 0
import collections
for l in lines:
    def go(line):
        SEEN = set()
        Q = collections.deque([('',0,(3,2),(0,2),(0,2))])
        while Q:
            trace,cost,(r1,c1),(r2,c2),(r3,c3) = Q.popleft()
            #print(trace,cost,(r1,c1),(r2,c2),(r3,c3))
            if not line.startswith( trace ):
                continue
            if line == trace:
                return cost
            curr = ( trace,r1,c1,r2,c2,r3,c3 )
            if curr in SEEN:
                continue
            SEEN.add( curr )
            if not getn(r1,c1) or not getdir(r2,c2) or not getdir(r3,c3):
                continue
            for btn in btns:
                updated = trace
                rr1,cc1=r1,c1
                rr2,cc2=r2,c2
                rr3,cc3,nextbtn = nextdir(r3,c3,btn)
                if nextbtn:
                    rr2,cc2,nextbtn = nextdir(r2,c2,nextbtn)
                    if nextbtn:
                        rr1,cc1,nextbtn = nextn(r1,c1,nextbtn)
                        if nextbtn:
                            updated += nextbtn
                Q.append( (updated,cost + 1,(rr1,cc1),(rr2,cc2),(rr3,cc3)) )
    res1 += go(l) * int(l[:-1])
#print('part 1:', res)

npos = {}
for r in range(4):
    for c in range(3):
        if NUMS[r][c]: npos[NUMS[r][c]] = (r,c)

dpos = {}
for r in range(2):
    for c in range(3):
        if DIRS[r][c]: dpos[DIRS[r][c]] = (r,c)

def paths(S,E,where):
    def recursebackwards(s,e,where):
        #print(sr,sc,where)
        if s == e:
            return ['A']
        if where == 'NUM' and s not in npos.values() \
        or where == 'DIR' and s not in dpos.values():
            return []
        res = []
        sr,sc = s
        er,ec = e
        if sr > er:
            news = (sr - 1, sc)
            P = recursebackwards(news,e,where)
            res += [p + '^' for p in P]
        if sr < er:
            news = (sr + 1, sc)
            P = recursebackwards(news,e,where)
            res += [p + 'v' for p in P]
        if sc > ec:
            news = (sr, sc - 1)
            P = recursebackwards(news,e,where)
            res += [p + '<' for p in P]
        if sc < ec:
            news = (sr, sc + 1)
            P = recursebackwards(news,e,where)
            res += [p + '>' for p in P]
        return res
    res = recursebackwards(S,E,where)
    return [_[::-1] for _ in res]

cache = {}
def p2(skey,ekey,level):
    if level == 26: return 1
    if (skey,ekey,level) in cache: return cache[(skey,ekey,level)]
    res = 10**20
    if level != 0:
        spos,epos,where = dpos[skey],dpos[ekey],'DIR'
    else:
        spos,epos,where = npos[skey],npos[ekey],'NUM'
    P = paths(spos,epos,where)
    for p in P:
        size = 0
        start = 'A'
        for end in p:
            size += p2(start,end,level + 1)
            start = end
        res = min(res,size)
    cache[(skey,ekey,level)] = res
    return res

res2 = 0
for l in lines:
    size = 0
    start = 'A'
    for end in l:
        size += p2(start, end, 0)
        start = end
    res2 += int(l[:3]) * size

print('part 1:', res1)
assert res1 in[126384,215374]
print('part 2:', res2)
assert res2 in[260586897262600]
