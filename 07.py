def p1(t, nums, N, NG):
    for mask in range(2 ** NG): # for NG gaps we have 2^ng possibilities
        perm=[]
        res = nums[0]

        way1 = True
        if way1: # way 1/ rightshift Left index by i-1
            for i in range(1, N):
                if (mask >> (i - 1)) & 1 == 1: # r-shift
                    res *= nums[i]
                    perm.append('1 ')
                else:
                    res += nums[i]
                    perm.append('o ')
        else: # way 2/ leftshift ...001 by i number of bits
            for i in range(N - 1):
                if (mask & (1 << i)) > 0: # l-shift
                    res *= nums[i + 1]
                    perm.append('1 ')
                else:
                    res += nums[i + 1]
                    perm.append('o ')
        if t == res:
            return True
    return False

"""
o o o
1 o o
o 1 o
1 1 o
o o 1
1 o 1
o 1 1
1 1 1
"""

lines = open(0).read().splitlines()
r1,r2=0,0
for line in lines:
    test, nums = line.split(': ')
    t, nums = int(test), [int(_) for _ in nums.split()]
    N = len(nums)
    NG = N - 1 # gaps = len - 1
    if p1 (t, nums, N, NG):
        r1 += t
    OK = False
    def p2(idx, curr):
        global OK
        if idx == N:
            if curr == t:
                OK = True
            return
        p2(idx + 1, curr + nums[idx])
        p2(idx + 1, curr * nums[idx])
        p2(idx + 1, int( str(curr) + str(nums[idx]) ))
    p2 (1, nums[0])
    if OK:
        r2 += t

print('part 1:', r1); assert(r1 in[2437272016585, 3749])
print('part 2:', r2); assert(r2 in[11387, 162987117690649])

