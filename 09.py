line = open(0).read().strip()
line = '2333133121414131402'#'12345'

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
    Q = makeQ()
    return res

part2 = p2()

# p1

def p1() -> int:
    Q = makeQ();print('a/', ''.join(str(_) for _ in Q))
    i = 0;
    while i < len(Q):
        while Q[i] == '.':
            Q[i] = Q.pop()
        i += 1
    print('a/', ''.join(str(_) for _ in Q))
    return sum( i * n for i, n in enumerate(Q))
part1 = p1()

print('part 1:', part1); assert(part1 % 1000 in [548, 928])
print('part 2:', part2); assert(part2 % 1000 in [311, 858])
