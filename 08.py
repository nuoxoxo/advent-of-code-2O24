import collections
g = open(0).read().splitlines()
R,C = len(g),len(g[0])
A = collections.defaultdict(set)
for r, row in enumerate(g):
    for c, char in enumerate(row):
        if char != '.':
            A[(char)].add((r, c))
#print(A)
nodes = set()
nodes2 = set()
for cset in A.values():
    coor = sorted(list(cset))
    for r,c in coor:
        for rr, cc in coor:
            if rr == r and cc == c: continue
            dr, dc = rr - r, cc - c
            if r - dr in range(R) and c - dc in range(C):
                nodes.add((r - dr, c - dc))
            if rr + dr in range(R)and cc + dc in range(C):
                nodes.add((rr + dr, cc + dc))
            # PART 2
            i, j = r, c
            t = -1
            while 42:
                t += 1
                found = False
                if i + dr * t in range(R) and j + dc * t in range(C):
                    nodes2.add((i + dr * t, j + dc * t))
                    found = True
                if i - dr * t in range(R) and j - dc * t in range(C):
                    nodes2.add((i - dr * t, j - dc * t))
                    found = True
                if not found: break
print('part 1:', len(nodes))
print('part 2:', len(nodes2))
