lines = open(0).read().strip().split('\n')
r1, r2 = 0, 0
for line in lines:
    a = [int(_) for _ in line.split()]

    def ok(a) -> bool:
        res = 0
        aa = sorted(a)
        if (a == aa or a == aa[::-1]) and len(a) == len(set(a)):
            gap = 0
            for i in range(1, len(a)):
                gap = max(gap, abs(a[i] - a[i-1]))
                if gap > 3:
                    break
            if gap in [1,2,3]:
                res += 1
        return res

    if ok (a):
        r1 += 1
    else:
        for i in range(len(a) - 1):
            aa = a[:i] + a[i + 1:]
            if ok (aa):
                r2 += 1
print('part 1:', r1)
print('part 2:', r1 + r2)
