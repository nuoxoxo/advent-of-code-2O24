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

def part2() -> int:
    res = 0
    Q = makeQ();print(''.join(str(_) for _ in Q), '/B\n')
    i = 0
    SPACE, IDS = [], {}
    N = len(Q)
    highest = None
    while 42:
        if Q[i] == '.':
            count = 0
            start = i
            while i < N and Q[i] == '.':
                count, i = count + 1, i + 1
            if count != 0:
                SPACE.append( (start, count) )
            if i >= N:
                break
        else:
            count = 0
            start, curr = i, Q[i]
            while i < N and Q[i] == curr:
                count, i = count + 1, i + 1
            if count != 0:
                IDS[int(curr)] = ( start, count )
            highest = int(curr)
            if i >= N:
                break
    # moving files
    while highest > -1:
        left, numsize = IDS[highest]
        for i, (start,spacesize) in enumerate(SPACE):
            if start > left: break
            if numsize == spacesize:
                IDS[highest] = (start, numsize)
                SPACE[i] = (start + numsize, 0)
                break
            if numsize < spacesize:
                IDS[highest] = (start, numsize)
                SPACE[i] =(start + numsize, spacesize - numsize)
                break
        highest -= 1
    return sum( i * n for n, (L, N) in IDS.items() for i in range(L, L + N))

def part1() -> int:
    Q = makeQ();print('A/', ''.join(str(_) for _ in Q))
    i = 0;
    while i < len(Q):
        while Q[i] == '.':
            Q[i] = Q.pop()
        i += 1
    print('A/', ''.join(str(_) for _ in Q))
    return sum( i * n for i, n in enumerate(Q))

p1, p2 = part1(), part2()
print('part 1:', p1); assert(p1 % 1000 in [548, 928])
print('part 2:', p2); assert(p2 % 1000 in [311, 858])

