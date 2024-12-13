lines = open(0).read().strip().split('\n\n')
import re
import numpy
from sympy import symbols, Eq, solve
for i,line in enumerate(lines):print(line, '/', i)
p1=0
p2=0
for _,line in enumerate(lines):
    btn = []
    for l in line.splitlines():
        btn.append(list(map(int, re.findall(r'\d+', l))))
    A,B,P = btn
    P2 = [P[0]+10000000000000,P[1]+10000000000000]
    def go2(A,B,P):
        # just solve the systems of EQ
        #print(_, '/', A,B,P)
        #global p2
        a, b = symbols('a b', integer=True)
        up = Eq( a*A[0] + b*B[0], P[0])
        down = Eq( a*A[1] + b*B[1], P[1])
        res = solve((up, down), (a, b))
        if res:
            #print(res)
            #p2 += res[a]*3 + res[b]
            return res[a]*3 + res[b]
        return 0
        """
        coef = numpy.array([[A[0],B[0]], [A[1],B[1]]])
        end = numpy.array(P)
        res = numpy.linalg.solve(coef, end)
        print(_, '/', res)
        if numpy.all(res == res.astype(int)):
        #if isinstance(a, int) and isinstance(b, int):
            a,b = tuple(res.astype(int))
            if a > -1 and b > -1:
                p2 += 3*a + b
                print(a,b)
        """
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
                    #print(p1)
                    return
                if ex > X or ey > Y:
                    break
            if a > limA:
                return
    #go(A,B,P)#P2)
    p2 += go2(A,B,P2)
    p1 += go2(A,B,P)
print(p1)
print(p2)
