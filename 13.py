lines = open(0).read().strip().split('\n\n')
import re
for i,line in enumerate(lines):print(line, '/', i)
p1=0
p2=0
for _,line in enumerate(lines):
    btn = []
    for l in line.splitlines():
        btn.append(list(map(int, re.findall(r'\d+', l))))
    A,B,P = btn
    P2 = [P[0]+10000000000000,P[1]+10000000000000]
    print(_, '/', A,B,P)
    # B is cheaper, so loop A first
    
    def go(A,B,P):
        global p1
        X,Y=P
        a = -1
        # whats the limit
        limA = max(P[0] // A[0], P[1] // A[1])
        limB = max(P[0] // B[0], P[1] // B[1])
        while 42:
            a, b = a + 1, 0
            while 42:
                b += 1
                #print(a,b)
                ex, ey = a * A[0] + b * B[0], a * A[1] + b * B[1]
                if ex == X and ey == Y:
                    p1 += a*3 + b
                    print(p1)
                    return
                if ex > X or ey > Y:
                    break
            if a > limA:
                return
    go(A,B,P2)
print(p1)
