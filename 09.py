line = open(0).read().strip()
#line = '2333133121414131402'#'12345'

def p2() -> int:
    res = 0
    return res

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
