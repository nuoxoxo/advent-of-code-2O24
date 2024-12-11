a = [int(_) for _ in open(0).read().split()]
print(a)#for n in a:print(n)
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
print(len(A))#$, '-', A)
