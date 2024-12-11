B=75#25
testing=not False
a = [int(_) for _ in open(0).read().split()]
print(a)

def p2() -> int:
    from collections import Counter
    b = 0
    counter = Counter(a)
    while 42:
        tmp = Counter()
        if testing:print(b)
        if b == B:
            break
        for k, n in counter.items():
        #for n in a:
            if k == 0:
                tmp[1] += n#A.append(1)
            elif len(str(k)) % 2 == 0:
                N = len(str(k))
                tmp[int(str(k)[:N // 2])] += n#A.append(int(str(n)[:N // 2]))
                tmp[int(str(k)[N // 2:])] += n#A.append(int(str(n)[N // 2:]))
            else:
                tmp[k * 2024] += n#A.append(n * 2024)
        b+=1
        counter = tmp
    return sum(counter.values())#len(A)

def p1(a) -> int:
    b = 0
    while 42:
        if testing:print(b)
        if b == 25:
            break
        A = []
        for n in a:
            if n == 0:
                A.append(1)
            elif len(str(n)) % 2 == 0:
                N = len(str(n))
                A.append(int(str(n)[:N // 2]))
                A.append(int(str(n)[N // 2:]))
            else:
                A.append(n * 2024)
        b+=1
        if testing: print(b, '-', len(A), '-', A)
        a = A[:]
    return len(A)

res1,res2 = p1(a), p2()
print('part 1:', res1);
print('part 2:', res2);
