patt,lines = open(0).read().strip().split('\n\n')
patt = patt.split(', ')
ps = set(patt)
assert len(ps)==len(patt)
res = 0
res2 = 0
for line in lines.splitlines():
    print(line)
    dp = {}
    def go(w) -> int:
        if not w: return 1
        if w in dp: return dp[w]
        here = 0
        for p in ps:
            if w.startswith(p): here += go(w[len(p): ])
        dp[w] = here
        return here
    g = go(line)
    res += (g > 0)
    res2 += g
print(res, res2)
