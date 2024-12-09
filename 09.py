line = open(0).read().strip()
#line = '2333133121414131402'#'12345'
Q = []
curr = 0
for i, c in enumerate(line):
    if i % 2 == 0:
        for _ in range(int(c)):Q.append(curr)
        curr += 1
    else:
        for _ in range(int(c)):Q.append(None)
#print(Q)
i = 0
while i < len(Q):
    if Q[i] is not None:
        i += 1
    else:
        while Q[i] is None:
            Q[i] = Q.pop()
            #i += 1
        #print(Q)
#print(Q)
print(sum( i * n for i, n in enumerate(Q)))
