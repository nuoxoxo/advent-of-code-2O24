def schm(bl):
    return [ l.count('#') - 1 for l in list(zip(*bl)) ]
B = [_.split() for _ in open(0).read().strip().split('\n\n')]
L,K = [_ for _ in B if _[0] == '#'*5], [_ for _ in B if _[-1] == '#'*5]
print(sum(all([a+b < 6 for a,b in zip(schm(k),schm(l))]) for k in K for l in L))
