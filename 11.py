a = [int(_) for _ in open(0).read().split()]
print(a)#for n in a:print(n)

def p2() -> int:
    from collections import Counter
    b = 0
    counter = Counter(a)
    while 42:
        tmp = Counter()
        print(b)
        if b == 75:
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
        print(b)
        if b == 75:
            break
        A = []
        blinked = False
        #print('curr/', a)
        for n in a:
            if n == 0:
                #print('up/', b, n)
                A.append(1)
                blinked = True
                #print('curr/', A)
            elif len(str(n)) % 2 == 0:
                #print('mid/',b, n)
                N = len(str(n))
                A.append(int(str(n)[:N // 2]))
                A.append(int(str(n)[N // 2:]))
                blinked = True
                #print('curr/', A)
            else:
                #print('down/',b, n)
                A.append(n * 2024)
                blinked = True
                #print('curr/', A)
        b+=1
        #print(len(A), '-', A)
        a = A[:]
        if not blinked:
            break
    return len(A)


print(p2())
