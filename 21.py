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
res = 0
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
    res += go(l) * int(l[:-1])
print('res/', res)

