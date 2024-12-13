import re, sympy as sp, numpy as np
lines = open(0).read().strip().split('\n\n')
p1=0
p2=0
for _,line in enumerate(lines):
    btn = []
    for l in line.splitlines():
        btn.append(list(map(int, re.findall(r'\d+', l))))
    A,B,P = btn
    def byhand(A,B,X,Y) -> int:
        # solve a system of linear equations by hand
        #       a*A + b*B = (X, Y)
        #   determinant ---> check if A,B are linearly dependent
        #       determinant = ax*by - ay*bx 
        denom = A[0]*B[1] - A[1]*B[0]
        if denom == 0 or B[0] == 0:
            return 0
        #   apply cramer's rule
        #       a = (X*by - Y*bx) / dm
        #       b = (X    - a*ax) / bx
        a = (X*B[1] - Y*B[0]) / denom
        b = (X - A[0] * a) / B[0]
        if int(a) == a and int(b) == b:
            if a < 0 or b < 0:
                print('byhand/negative', a, b)
            return int(a)*3 + int(b)
        return 0
    def dosympy(A,B,X,Y) -> int: # sp
        a,b = sp.symbols('a b', integer=True)
        eq1 = sp.Eq( a*A[0] + b*B[0], X)
        eq2 = sp.Eq( a*A[1] + b*B[1], Y)
        res = sp.solve((eq1,eq2), (a,b))
        if res:
            if res[a] < 0 or res[b] < 0:
                print('sp/negative', a, b)
            return res[a]*3 + res[b]
        return 0
    def donumpy(A,B,X,Y) -> int: # hard to tune it right also the slowest
        mat = np.array([[A[0], B[0]], [A[1], B[1]]])#.astype(int)
        vec = np.array([X, Y])#.astype(int)
        res = np.linalg.solve( mat, vec )
        if np.all(np.abs(res - np.round(res)) < 1e-3):
            a, b = np.round(res).astype(int)
            return a*3 + b
        return 0
    def go(A,B,X,Y) -> int:
        res = 0
        X,Y=P
        a = -1
        lim = max(X // A[0], Y // A[1])
        while 42:
            a, b = a + 1, 0
            while 42:
                b += 1
                ex, ey = a * A[0] + b * B[0], a * A[1] + b * B[1]
                if ex == X and ey == Y:
                    return a*3 + b
                if ex > X or ey > Y:
                    break
            if a > lim:
                break
        return 0
    p2 += [byhand, dosympy, donumpy][0](A,B,\
        P[0]+10000000000000,P[1]+10000000000000)
    p1 += [byhand, dosympy, donumpy][0](A,B,P[0],P[1])
print('part 1:', p1);assert(p1 in [480, 27105])
print('part 2:', p2);assert(p2 == 101726882250942)
