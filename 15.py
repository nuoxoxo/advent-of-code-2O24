G,moves = open(0).read().split('\n\n')
G = [list(_.strip()) for _ in G.splitlines()]
#for g in G:print(' '.join(g), '/init')
moves = [_.strip() for _ in moves.splitlines()]
R,C=len(G),len(G[0])
D={'<': (0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}

def printer_row(g, curriter, msg):
    print(''.join(g), curriter, msg)

def printer(G, curriter, msg):
    for g in G: print(''.join(g), curriter, msg)
    print()

def solve(G, PART2=False):
    if PART2:
        for i in range(R): # transform grid
            row = []
            for c in G[i]:
                if c == '@': row += ['@', '.']
                if c == 'O': row += ['[', ']']
                if c == '#': row += ['#', '#']
                if c == '.': row += ['.', '.']
            G[i] = row;
            print(''.join(row),i,'line/final')
    r,c=None,None
    for i,g in enumerate(G):
        for j in range(len(g)):
            if g[j] == '@':
                r,c = i,j
                break
    assert(r and c)
    for g in G:print(''.join(g), '/init')
    for i,m in enumerate(moves):
        for j,ar in enumerate(m):
            dr,dc = D[ar]
            rr,cc = r,c
            stuck = False
            Q = [(r,c)]
            if PART2:
                dq = [(r,c)]
                while dq:
                    rr,cc = dq.pop(0)
                    rr,cc = rr + dr, cc + dc
                    if (rr,cc) in Q:
                        continue
                    thing = G[rr][cc]
                    if thing in '[]':
                        Q.append((rr,cc))
                        dq.append((rr,cc))
                        if thing == '[':
                            Q.append((rr,cc + 1))
                            dq.append((rr,cc + 1))
                        if thing == ']':
                            Q.append((rr,cc - 1))
                            dq.append((rr,cc - 1))
                    elif thing == '#':
                        stuck = True
                        break
                if stuck:
                    continue
            else:
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
                if PART2:
                    G[br + dr][bc + dc] = G[br][bc]
                else:
                    G[br + dr][bc + dc] = 'O'
                G[br][bc] = '.'
            G[r + dr][c + dc] = '@' # mave myself
            G[r][c] = '.' # left null
            r, c = r + dr, c + dc
        printer(G, i, 'iter/evol')
    res = 0
    symbol = '[' if PART2 else 'O' # part2
    for r,g in enumerate(G):
        for c,thing in enumerate(g):
            if thing == symbol:
                res += 100 * r + c
        printer_row(''.join(g), r, 'line/final')
    return res

p1 = solve([_[:] for _ in G])
p2 = solve(G, True)
print('part 1:', p1)
print('part 2:', p2);assert(p1 in [10092, 1527563] and p2 in [9021, 1521635])
