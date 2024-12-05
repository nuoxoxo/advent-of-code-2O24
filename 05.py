from collections import defaultdict
U,D = open(0).read().split('\n\n')

isafter = defaultdict(set)#set()
for l in U.split():
    bef, af = [int(_) for _ in l.split('|')]
    isafter[bef].add(af)
p2,p1 = 0,0

from functools import cmp_to_key
def part2(l,r) -> int:
    if l in isafter[r]:
        return -1
    if r in isafter[l]:
        return 1
    return 0

for l in D.split():
    A = [int(_) for _ in l.split(',')]
    N = len(A)
    ok = True
    for l in range(N):
        for r in range(N):
            if l < r and A[l] in isafter[A[r]]:
                ok = False
    if not ok:
        A.sort(key=cmp_to_key(part2))
        p2 += A[N // 2]
    else:
        p1 += A[N // 2]
print('part 1:', p1)
print('part 2:', p2)

