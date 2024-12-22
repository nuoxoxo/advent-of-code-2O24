def mix(curr, src):
    return (curr ^ src)
def prune(curr):
    return (curr % 16777216)
def mp(curr, src):
    return prune(mix(curr, src))
def nthsecret(it, a):
    res = []
    for _ in range(it):
        b = mp(a * 64, a)
        c = mp(b // 32, b)
        a = mp(c * 2048, c)
        res.append(a)
    return res
print(mix(15,42)); print(prune(100000000))
for i,n in enumerate(nthsecret(10, 123)):print(f'{i}/ {n}')

p1=0
nums = list(map(int,open(0).read().splitlines()))
for n in nums: p1 +=nthsecret(2000, n)[-1]

def nsp2(it,a):
    secrets, diffs = [],[]
    prev = a
    for _ in range(it):
        b = mp(a * 64, a)
        c = mp(b // 32, b)
        n = mp(c * 2048, c)
        diff = n%10 - prev%10
        diffs.append(diff)#n%10 - (prev%10))
        #print(f'{n%10} ({diff})')
        prev = n%10
        a = n
        secrets.append(n%10)
    return diffs,secrets
print(nsp2(10,123)); print('DBG/ends\n')
# try/ 2024 test input

import collections
D = collections.defaultdict(int)
for n in nums:
    a,b = nsp2(2000,n)
    """test = [-2,1,-1,3]
    for i in range(3,len(a)):
        if a[i-3:i+1] == test:
            print(f'found {b[i]} at {i} - {n}')
    """
    dd = collections.defaultdict(list)
    for i in range(3,len(a)):
        k = tuple(a[i-3:i+1])
        dd[k].append(b[ i ])
    for k,v in dd.items(): D[k] += v[0]
p2 = max(D.values())# 2103 lo

print('part 1:', p1)
print('part 2:', p2)
assert p1 in[37327623,19150344884]
assert p2 in[23,2121]
