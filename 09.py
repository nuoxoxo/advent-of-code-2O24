line = open(0).read().strip()
#line = '2333133121414131402'#'12345'

from collections import defaultdict
def p2() -> int:
    F, SP = defaultdict(tuple), []
    curr, left = 0, 0
    for i, c in enumerate(line):
        n = int(c)
        if i % 2 == 0:
            #F.append( (curr, left, n) )
            F[curr] = (left, left + n)
            curr += 1
        elif n != 0:
            SP.append( (left, left + n) )
        left += n
    #print(F, '/F -', len(F))
    #print(F.keys(), 'F/keys')
    #print(SP, '/SP -', len(SP))
    for curr in range(len(F) - 1, -1, -1):
        cbegin, cend = F[curr]; #print('f/', curr, currleft, Ncurr)
        for i, (spbegin, spend) in enumerate(SP[:]):
            Ncurr = cend - cbegin
            Nspace = spend - spbegin
            if Nspace == Ncurr: # replace
                F[curr] = (spbegin, spbegin + Ncurr)
                SP.pop(i)
                break
            elif Nspace > Ncurr: # insert
                F[curr] = (spbegin, spbegin + Ncurr)
                L, R = spbegin + Ncurr, spbegin + Nspace
                SP[i] = (L, R)
                break
            if cbegin <= spbegin:
                SP = SP[:i]
                break
        #print('sp/', SP)
    #print(sorted(list(F.items())))
    return sum( i * n for n, (L, R) in F.items() for i in range(L, R) )

Q = []
curr = 0
for i, c in enumerate(line):
    if i % 2 == 0:
        for _ in range(int(c)):
            Q.append(curr)
        curr += 1
    else:
        for _ in range(int(c)):
            Q.append(None)
i = 0;#print(Q)
while i < len(Q):
    if Q[i] is not None:
        i += 1
    else:
        while Q[i] is None:
            Q[i] = Q.pop()
        i += 1

part1 = sum( i * n for i, n in enumerate(Q))
part2 = p2()
print('part 1:', part1); assert(part1 % 1000 in [548, 928])
print('part 2:', part2); assert(part2 % 1000 in [311, 858])
