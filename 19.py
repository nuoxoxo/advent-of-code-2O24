patt,lines = open(0).read().strip().split('\n\n')
patt = patt.split(', ')
ps = set(patt)
assert len(ps)==len(patt)
res = 0
res2 = 0
for line in lines.splitlines():
    dp = {}
    def go(w) -> int: # original soln
        if not w: return 1
        if w in dp: return dp[w]
        here = 0
        for p in ps:
            if w.startswith(p):
                here += go(w[len(p): ])
        dp[w] = here
        return here

    def go2(i) -> int:
        if i == len(line): return 1
        if i in dp: return dp[i]
        here = 0
        for p in ps:
            if line[i:].startswith(p):
                here += go2(i + len(p))
        dp[i] = here
        return here

    def go3(): #sliding_window() -> int:
        dp = [0] * (len(line) + 1)
        dp[0] = 1
        for R in range(1, len(line) + 1):
            for p in ps:
                sub = line[ R - len(p) : R]
                if sub == p:
                    dp[R] += dp[ R - len(p)]
        return dp[len(line)]

    #g = go(line)
    #g = go2(0)
    g = go3()
    res += (g > 0)
    res2 += g
print('part 1:', res)
print('part 2:', res2)
assert res in [6, 306]
assert res2 in [16,604622004681855]
