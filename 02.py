lines = open(0).read().strip().split('\n')
r1, r2 = 0, 0
poss = 0
A,B=[],[]
for l in lines:
    a = [int(_) for _ in l.split()]
    def issafe(a) -> (bool, int):
        N = len(a)
        safe = True
        gap = 0
        for s in range(1, N): # find start
            if a[s - 1] < a[s]: # inc
                for i in range(s, N):
                    gap = max(abs(a[i - 1] - a[i]), gap)
                    if a[i - 1] > a[i]:
                        safe = False
                        idx = i
                        break
            elif a[s - 1] > a[s]: # dec
                for i in range(s, N):
                    gap = max(abs(a[i - 1] - a[i]), gap)
                    if a[i - 1] < a[i]:
                        safe = False
                        idx = i
                        break
            else:
                idx = s - 1
                safe = False
            if not safe or gap not in range(1, 4):
                break
        return (safe and gap in range(1,4), idx)
    check, pos = issafe(a)
    if check:
        r1 += 1
    else:
        icorr = -1
        for i in range(len(a)):
            aa = a[:i] + a[i + 1:]
            if issafe(aa)[0]:
                poss += 1
                icorr = i
                B.append(icorr) 
                A.append(pos)
                break
# 578 573 569/lo
r2 = r1 + poss
print('part 1:', r1)
print('part 2:', r2)
for a, b in zip(A, B):
    print(a,b)
"""
    elif pos > -1:
        print(pos)
        for p in [0, pos, len(a) - 1]:
            aa = a[::]
            aa.pop(p)
            if issafe(aa)[0]:
                poss += 1
                print(l, '-', aa)
                break
"""
