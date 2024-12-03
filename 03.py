import re
lines = open(0).read().strip().split('\n')
r2,r1 = 0,0
ok = True
for l in lines:
    for i in range(len(l)):
        sub = l[i:]
        if sub.startswith('do()'): ok = True
        if sub.startswith('don\'t()'): ok = False
        if l[i:].startswith('mul('):
            m = re.match(r'mul\((\d+,\d+)\)', l[i:])
            if not m: continue
            L, R = [int(_)for _ in m.group(1).split(',')]
            r1 += L*R
            r2 += L * R if ok else 0
print(len(lines), r1, r2)

