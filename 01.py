lines = open(0).read().strip().split('\n')

L, R = zip(*(map(int, _.split()) for _ in lines))
# a simpler way to get L R
"""
L, R = [], []
for line in lines:
    l, r = [int(_) for _ in line.split()]
    L.append(l)
    R.append(r)
"""
A, B = 0, 0
for l, r in zip(sorted(L), sorted(R)):
    A += abs(l - r)
    B += R.count(l)* l 
print('part 1:', A)
print('part 2:', B)
