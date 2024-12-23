import collections
ADJ = collections.defaultdict(list)
for l,r in [_.split('-') for _ in open(0).read().splitlines()]:
    ADJ[l].append(r)
    ADJ[r].append(l)
p1 = 0
A = list(ADJ.keys())
N = len(A)
t = 't'
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            a,b,c = A[i],A[j],A[k]
            aa,bb,cc = ADJ[a],ADJ[b],ADJ[c]
            if a in bb and b in cc and c in aa:
                p1 += any([a.startswith(t),b.startswith(t),c.startswith(t)])#:

def find_cliques(ADJ):
    cliq = []
    def bronkerbosch(possible_nodes,excluded_nodes,current_clique):
        if not possible_nodes and not excluded_nodes:
            cliq.append(current_clique)
            return
        for node in list(possible_nodes):
            bronkerbosch (
                possible_nodes.intersection(ADJ[node]),
                excluded_nodes.intersection(ADJ[node]),
                current_clique.union(set([node]))
            )
            possible_nodes.remove(node)
            if node in excluded_nodes:
                excluded_nodes.remove(node)
    bronkerbosch (set(ADJ.keys()),set(),set() )
    return cliq

"""def find_cliques(ADJ):
    SEEN = set()
    def DFS(cliqueset, node):
        cliqueset.add(node)
        SEEN.add(node)
        for neig in ADJ[node]:
            if neig not in SEEN: DFS(cliqueset, neig)
    cliq = []
    for node in ADJ.keys():
        if node in SEEN: continue
        cliqueset = set()
        DFS(cliqueset,node)
        if len(cliqueset) > 1:
            cliq.append(cliqueset)
    return cliq"""

p2 = ','.join(sorted(max(list(find_cliques(ADJ)),key=len)))

print('part 1:', p1)
print('part 2:', p2)
assert p1 in [1308,7,3]
assert p2.startswith('bu,fq')

