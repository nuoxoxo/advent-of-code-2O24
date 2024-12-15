G,moves = open(0).read().split('\n\n')
G = [list(_.strip()) for _ in G.splitlines()]
#p2
"""
for i in range(len(G)):
    temp = []
    for c in G[i]:
        if c == '@':
            temp.append('@')
            temp.append('.')
        if c == 'O':
            temp.append('[')
            temp.append(']')
        if c == '#':
            temp.append('#')
            temp.append('#')
        if c == '.':
            temp.append('.')
            temp.append('.')
    G[i] = temp
"""
for g in G:print(' '.join(g), '/init')
moves = [_.strip() for _ in moves.splitlines()]
#w,b = set(),[]#set()

"""
sr,sc=None,None
for r,g in enumerate(G):
    for c in range(len(g)):
        if g[c] == '@':
            sr,sc = r, c
            break
"""
        #if g[c] == 'O': b.append((r,c))#add((r,c))
        #if g[c] == '#': w.add((r,c))

R,C=len(G),len(G[0])
D={'<': (0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}

def p2(G):
    # transform grid
    for i in range(len(G)):
        temp = []
        for c in G[i]:
            if c == '@':
                temp.append('@')
                temp.append('.')
            if c == 'O':
                temp.append('[')
                temp.append(']')
            if c == '#':
                temp.append('#')
                temp.append('#')
            if c == '.':
                temp.append('.')
                temp.append('.')
        G[i] = temp
    # new start
    sr,sc=None,None
    for r,g in enumerate(G):
        for c in range(len(g)):
            if g[c] == '@':
                sr,sc = r, c
                break
    for g in G:print(' '.join(g), '/init')
    r,c=sr,sc
    print(sr,sc,r,c)
    for i,m in enumerate(moves):
        #print(m,i)
        for j,ar in enumerate(m):
            dr,dc = D[ar]
            #rr,cc = r + dr, c + dc
            #print('nxt/', rr,cc)
            #print(r,c)
            Q = [(r,c)]
            todoset = [(r,c)]
            rr,cc = r,c
            stuck = False
            # p2
            #"""
            #for rr,cc in Q:#while 42:
            while Q:
                rr,cc = Q.pop(0)
                rr,cc = rr + dr, cc + dc
                if (rr,cc) in todoset:
                    continue
                #print(rr,cc,Q)
                thing = G[rr][cc]
                if thing in '[]':
                    #Q.append((rr,cc))
                    #if thing == '[': Q.append((rr,cc + 1))
                    Q.append((rr,cc))
                    todoset.append((rr,cc))
                    if thing == '[':
                        Q.append((rr,cc + 1))
                        todoset.append((rr,cc + 1))
                    if thing == ']':
                        todoset.append((rr,cc - 1))
                        Q.append((rr,cc - 1))
                    #if thing == ']': Q.append((rr,cc - 1))
                if thing == '#':
                    stuck = True
                    break
            # p1
            """
            while 42:
                rr,cc = rr + dr, cc + dc
                thing = G[rr][cc]
                if thing == '.': break
                if thing == 'O': Q.append((rr,cc))
                if thing == '#':
                    stuck = True
                    break
            """
            if stuck:
                continue

            #p2
            Q = todoset
            gg = [_[:] for _ in G]
            for k in range(len(Q) - 1):
                br,bc = Q[k + 1]
                G[br][bc] = '.'
            for k in range(len(Q) - 1):
                br,bc = Q[k + 1]
                rr,cc = br + dr, bc + dc
                G[rr][cc] = gg[br][bc]
            #p1
            """
            for k in range(len(Q) - 1):
                br,bc = Q[k + 1]
                rr,cc = br + dr, bc + dc
                G[rr][cc] = 'O'
            """
            G[r + dr][c + dc] = '@' # move to ball
            G[r][c] = '.' # left null
            r,c = r + dr,c + dc
        #for k,g in enumerate(G):print(' '.join(g),i,'iter/evol')
        print()

    res = 0
    res2=0
    for r,g in enumerate(G):
        for c,thing in enumerate(g):
            if thing == 'O': res += 100*r+c
            if thing == '[': res2 += 100*r+c
        print(' '.join(g),r)
    #print(res)
    #print(res2)
    return res2

def p1(G):
    sr,sc=None,None
    for r,g in enumerate(G):
        for c in range(len(g)):
            if g[c] == '@':
                sr,sc = r, c
                break
    r,c=sr,sc
    #print(sr,sc,r,c)
    for i,m in enumerate(moves):
        #print(m,i)
        for j,ar in enumerate(m):
            dr,dc = D[ar]
            #rr,cc = r + dr, c + dc
            #print('nxt/', rr,cc)
            #print(r,c)
            todo = [(r,c)]
            rr,cc = r,c
            stuck = False
            while 42:
                rr,cc = rr + dr, cc + dc
                thing = G[rr][cc]
                if thing == '.': break
                if thing == 'O': todo.append((rr,cc))
                if thing == '#':
                    stuck = True
                    break
            if stuck:
                continue
            for k in range(len(todo) - 1):
                br,bc = todo[k + 1]
                rr,cc = br + dr, bc + dc
                G[rr][cc] = 'O'
            # wrong
            """
            if not (-1<rr<R and -1<cc<C) or (rr,cc) in w:
                continue
            changed = False
            for k,pos in enumerate(b):
                if pos == (rr,cc):
                    #print(r,c,'-',rr,cc,'-',pos)
                    br,bc = pos
                    brr,bcc = br + dr, bc + dc
                    if not (-1<brr<R and -1<bcc<C) or (rr,cc) in w or (rr,cc) in b:
                        changed = True
                        break
                    b[k] = (brr,bcc)
                    r,c = rr,cc
                    changed = True
                    break
            if not changed:
                r,c = rr,cc
            print(r,c)
            """
            G[r + dr][c + dc] = '@' # move to ball
            G[r][c] = '.' # left null
            r,c = r + dr,c + dc
        #for k,g in enumerate(G):print(' '.join(g),i,'iter/evol')
        print()

    res = 0
    for r,g in enumerate(G):
        for c,thing in enumerate(g):
            if thing == 'O': res += 100*r+c
        #print(' '.join(g),r, 'line/end')
    print()
    return res

res1 = p1(G[:])
res2 = p2(G[:])
print('part 1:', res1)
print('part 2:', res2)
assert(res1 in [10092, 1527563])
assert(res2 in [9021, 1521635])

