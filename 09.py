line = open(0).read().strip()
#line = '2333133121414131402'#'12345'

def makeQ():
    q = []
    curr = 0
    for i, c in enumerate(line):
        if i % 2 == 0:
            for _ in range(int(c)): q.append(curr)
            curr += 1
            continue
        for _ in range(int(c)): q.append('.')
    return q

def p2() -> int:
    res = 0
    Q = makeQ();print(''.join(str(_) for _ in Q), '/B\n')
    i = 0
    SPACE, IDS = [], {}
    N = len(Q)
    highest = None
    while 42:
        # counting spaces
        if Q[i] == '.':
            count = 0
            start = i
            while i < N and Q[i] == '.':
                count, i = count + 1, i + 1
            if count != 0:
                SPACE.append( (start, count) )
            if i >= N:
                break
        # counting numbers
        else:
            count = 0
            start, curr = i, Q[i]
            while i < N and Q[i] == curr:
                count, i = count + 1, i + 1
            if count != 0:
                #IDS.append( (curr, start, count) )
                IDS[int(curr)] = ( start, count )
            highest = int(curr)
            if i >= N:
                break
    # moving whole files
    highest_saved = highest
    while highest > -1:
        left, numsize = IDS[highest]
        for i, (start,spacesize) in enumerate(SPACE):
            if start > left: break
            if numsize == spacesize:
                IDS[highest] = ( start, numsize )# update IDS
                SPACE[i] = ( start + numsize, 0 )# update SPACE
                break
            if numsize < spacesize:
                IDS[highest] = ( start, numsize )# upd IDS
                SPACE[i] = ( start + numsize, spacesize - numsize )# upd SPACE
                break
        highest -= 1
    i = 0
    for k, (start, size) in IDS.items():
        for j in range(start, start + size):
            res += j * k
    return res

part2 = p2()

print('sample/\n' + """00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
""")

# p1

def p1() -> int:
    Q = makeQ();print('A/', ''.join(str(_) for _ in Q))
    i = 0;
    while i < len(Q):
        while Q[i] == '.':
            Q[i] = Q.pop()
        i += 1
    print('A/', ''.join(str(_) for _ in Q))
    return sum( i * n for i, n in enumerate(Q))
part1 = p1()

print('part 1:', part1); assert(part1 % 1000 in [548, 928])
print('part 2:', part2); assert(part2 % 1000 in [311, 858])


