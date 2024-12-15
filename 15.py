G,moves = open(0).read().split('\n\n')
G = [list(_.strip()) for _ in G.splitlines()]
#for g in G:print(' '.join(g), '/init')
moves = [_.strip() for _ in moves.splitlines()]
R,C=len(G),len(G[0])
D={'<': (0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}

def p2(G):
    for i in range(R): # transform grid
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
    for g in G:print(''.join(g), '/init')
    r,c=sr,sc
    for i,m in enumerate(moves):
        for j,ar in enumerate(m):
            dr,dc = D[ar]
            Q = [(r,c)]
            todoset = [(r,c)]
            rr,cc = r,c
            stuck = False
            while Q:
                rr,cc = Q.pop(0)
                rr,cc = rr + dr, cc + dc
                if (rr,cc) in todoset:
                    continue
                thing = G[rr][cc]
                if thing in '[]':
                    Q.append((rr,cc))
                    todoset.append((rr,cc))
                    if thing == '[':
                        Q.append((rr,cc + 1))
                        todoset.append((rr,cc + 1))
                    if thing == ']':
                        todoset.append((rr,cc - 1))
                        Q.append((rr,cc - 1))
                if thing == '#':
                    stuck = True
                    break
            if stuck:
                continue
            Q = todoset
            gg = [_[:] for _ in G]
            for k in range(len(Q) - 1):
                br,bc = Q[k + 1]
                G[br][bc] = '.'
            for k in range(len(Q) - 1):
                br,bc = Q[k + 1]
                rr,cc = br + dr, bc + dc
                G[rr][cc] = gg[br][bc]
            G[r + dr][c + dc] = '@' # move to ball
            G[r][c] = '.' # left null
            r,c = r + dr,c + dc
        """for k,g in enumerate(G):print(' '.join(g),i,'iter/evol')
        print()
        """
    res = 0
    for r,g in enumerate(G):
        for c,thing in enumerate(g):
            if thing == '[': res += 100 * r + c
        #print(' '.join(g),r)
    return res

def p1(G):
    sr,sc=None,None
    for r,g in enumerate(G):
        for c in range(len(g)):
            if g[c] == '@':
                sr,sc = r, c
                break
    for g in G:print(' '.join(g), '/init')
    r,c=sr,sc
    for i,m in enumerate(moves):
        for j,ar in enumerate(m):
            dr,dc = D[ar]
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
            G[r + dr][c + dc] = '@' # move to ball
            G[r][c] = '.' # left null
            r,c = r + dr,c + dc
        """or k,g in enumerate(G):print(' '.join(g),i,'iter/evol')
        print()
        """
    res = 0
    for r,g in enumerate(G):
        for c,thing in enumerate(g):
            if thing == 'O': res += 100*r+c
        #print(' '.join(g),r, 'line/end')
    return res

res1 = p1([_[:] for _ in G])
res2 = p2(G)
print('part 1:', res1)
print('part 2:', res2)
assert(res1 in [10092, 1527563])
assert(res2 in [9021, 1521635])

