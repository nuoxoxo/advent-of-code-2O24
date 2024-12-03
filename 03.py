import re
lines = open(0).read().strip().split('\n')
r2,r1 = 0,0
ok = True

for l in lines:
    # p1
    ps = re.findall(r'mul\((\d+,\d+)\)', l)
    for p in ps:#pairs:
        L, R = [int(_)for _ in p.split(',')]
        r1 += L * R
    # p2
    ts = re.findall(r'mul\((\d+,\d+)\)|(do\(\))|(don\'t\(\))', l)
    for a, b, c in ts:#trios:
        if b: ok = True
        if c: ok = False
        if ok and a:
            L, R = [int(_)for _ in a.split(',')]
            r2 += L * R

print('part 1:', r1)
print('part 2:', r2)
assert(r1 == 160672468)
assert(r2 == 84893551)
