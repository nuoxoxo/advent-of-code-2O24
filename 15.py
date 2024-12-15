G,moves = open(0).read().split('\n\n')
G = [list(_.strip()) for _ in G.splitlines()]
#for g in G:print(' '.join(g), '/init')
moves = [_.strip() for _ in moves.splitlines()]
R,C=len(G),len(G[0])
D={'<': (0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}

def PrinterR(g, curriter, msg):
    print(''.join(g), curriter, msg)

def Printer(G, curriter, msg):
    for g in G: print(''.join(g), curriter, msg)
    print()

def p2(G):
    for i in range(R): # transform grid
        row = []
        for c in G[i]:
            if c == '@': row += ['@', '.']
            if c == 'O': row += ['[', ']']
            if c == '#': row += ['#', '#']
            if c == '.': row += ['.', '.']
        #print(''.join(g),r,'line/final')
        G[i] = row
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
            q2 = [(r,c)]
            Q = [(r,c)]
            rr,cc = r,c
            stuck = False
            while q2:
                rr,cc = q2.pop(0)
                rr,cc = rr + dr, cc + dc
                if (rr,cc) in Q:
                    continue
                thing = G[rr][cc]
                if thing in '[]':
                    q2.append((rr,cc))
                    Q.append((rr,cc))
                    if thing == '[':
                        q2.append((rr,cc + 1))
                        Q.append((rr,cc + 1))
                    if thing == ']':
                        q2.append((rr,cc - 1))
                        Q.append((rr,cc - 1))
                elif thing == '#':
                    stuck = True
                    break
            if stuck:
                continue
            gg = [_[:] for _ in G] # render new state
            while Q:
                br,bc = Q.pop()
                thing = G[br][bc]
                G[br][bc] = '.'
                G[br + dr][bc + dc] = thing
            G[r + dr][c + dc] = '@' # mave myself
            G[r][c] = '.' # left null
            r,c = r + dr,c + dc
        Printer(G, i, 'iter/evol')
    res = 0
    for r,g in enumerate(G):
        for c,thing in enumerate(g):
            if thing == '[': res += 100 * r + c
        PrinterR(''.join(g), r, 'line/final')
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
            Q = [(r,c)]
            rr,cc = r,c
            stuck = False
            while 42:
                rr,cc = rr + dr, cc + dc
                thing = G[rr][cc]
                if thing == '.': break
                if thing == 'O': Q.append((rr,cc))
                if thing == '#':
                    stuck = True
                    break
            if stuck:
                continue
            while Q:
                br,bc = Q.pop()
                G[br + dr][bc + dc] = 'O'
            G[r + dr][c + dc] = '@' # make the move
            G[r][c] = '.' # left null
            r,c = r + dr,c + dc

        Printer(G, i, 'iter/evol')
    res = 0
    for r,g in enumerate(G):
        for c,thing in enumerate(g):
            if thing == 'O': res += 100*r+c
        PrinterR(''.join(g), r, 'line/final')
    return res

res1 = p1([_[:] for _ in G])
res2 = p2(G)
print('part 1:', res1)
print('part 2:', res2)
assert(res1 in [10092, 1527563])
assert(res2 in [9021, 1521635])

