"""AND gates 
output 1 if both inputs are 1; 
if either input is 0, these gates output 0.
OR gates 
output 1 if one or both inputs is 1; 
if both inputs are 0, these gates output 0.
XOR gates 
output 1 if the inputs are different; 
if the inputs are the same, these gates output 0."""

up,down = open(0).read().strip().split('\n\n')
wires = {}
for line in up.splitlines():
    k,v = line.split(': ')
    wires[k] = int(v)
#for k in wires:print('wire/ -',k,wires[k])

while 42:
    ended = True
    for line in down.splitlines():
        A = line.split()
        a,code,b,_,c = A
        #print('gate/ -',a,code,b,c)
        if a not in wires or b not in wires:
            ended = False
            continue
        #print('passed/ -',a,code,b,c)
        tmp = None
        a,b = wires[a],wires[b]
        if code == 'AND': tmp = a & b
        elif code == 'OR': tmp = a | b
        elif code == 'XOR': tmp = a ^ b
        if c not in wires or wires[c] != tmp:
            ended = False
        wires[c] = tmp
        #if c[0] == 'z': print(c,tmp,'/res')
    if ended: break
resbin = ''
for k in sorted(wires.keys(), reverse=True):
    if k[0] == 'z':
        resbin += str(wires[k])
        print('z/end -',k,wires[k])
#for k in sorted(wires.keys()):print('end/ -',k,wires[k])
p1 = int(resbin, 2)

p2x,p2y = '',''
for k in sorted(wires.keys(), reverse=True):
    if k[0] in 'xy': print('xy/',k,wires[k])
    if k[0] == 'x': p2x += str(wires[k])
    elif k[0] == 'y': p2y += str(wires[k])
print('x/',p2x,int(p2x,2))
print('y/',p2y,int(p2y,2))

xyand,xyxor = [],[] # p1 - all and/xor gate w/ x inputs
nonxand,nonxxor = [],[]
allor = []
allzout = [] # to see if opcode is xor

f = open('24.x', 'a')
f2 = open('24.a', 'a')
f2.write('strict digraph {\n')
for line in down.splitlines():
    A = line.split()
    a,code,b,_,c = A
    # trying csa graph editor
    f.write(f'{a} {c}\n')
    f.write(f'{b} {c}\n')

    # try dot
    f2.write(f'  {a} -> {c} [label={code}]\n')
    f2.write(f'  {b} -> {c} [label={code}]\n')

    # try analyzing all AND and XOR gates
    gate = (a,code,b,c)
    if code == 'AND':
        if a[0] == 'x' or b[0] == 'x':
            xyand.append(gate)
        else:
            nonxand.append(gate)
    elif code == 'XOR':
        if a[0] == 'x' or b[0] == 'x':
            xyxor.append(gate)
        else:
            nonxxor.append(gate)
    elif code == 'OR':
        allor.append(gate)
    if c[0] == 'z':
        allzout.append(gate)

xyand.sort()
xyxor.sort()
observed = set()
observedz = set() # observed 2 checks if all Z ouputs come from xor except z45
observedor = set() # observed'or checks if any z.. outputs come from an OR gate
problematicZ = set()
for g in xyand: print('AND/xy',g)
for g in nonxand:
    print('AND/non-xy',g)
    if g[-1][0] == 'z':
        print('\t\t\t\t ^^^')
        observed.add(g[0])
        observed.add(g[2])
        problematicZ.add(g[-1])
for g in xyxor: print('XOR/',g)
for g in nonxxor:
    print('XOR/non-xy',g)
    if g[-1][0] != 'z':
        print('\t\t\t\t ^^^ - an xor gate should have an z outout')
        observedor.add(g[0])
        observedor.add(g[2])
for g in allor:
    print('OR/',g)
    if g[-1][0] == 'z' and g[-1] != 'z45':
        print('\t\t\t\t ^^^ - whether any z output comes from OR')
        observed.add(g[0])
        observed.add(g[2])
        problematicZ.add(g[-1])

print('poss/x/arr',observed)
for g in observed: print('possible/x',g)
for g in allzout:
    print('zout/',g)
    if g[1] != 'XOR' and '45' not in g[-1]:
        print('\t\t\t\t ^^^ - all z.. come from xor except z45 ')
        observedz.add(g[0])
        observedz.add(g[2])
        problematicZ.add(g[-1])
#print(','.join(sorted(list(observed))))

# z17 ?? -- fkb rcc
observedz |= set(['nnr','rqf'])
print(observedz)
print(','.join(sorted(list(observedz))))
#print(','.join(sorted(list(observedor))))
"""S = observed.union(observedz)
print(','.join(sorted(list( S ))), '/observed + observedz')
S = S.union(observedor)
print(','.join(sorted(list( S ))), '/prev + observedor')
"""
#S = observed.union(observedor)
#print(','.join(sorted(list( S ))), '/observed + observedor')
print(','.join(sorted(list( problematicZ ))), '/problematic zouts')

print('p1/',p1); assert p1 in[4,2024,53325321422566]

# z/ 16 31 37 - from observedz
# z/ 21 - from seeing with eyes
e = ['rrn','z37','rdn','z31','z16','fkb','rqf','nnr']
print('p2/',','.join(sorted(e)), '/eyes')
assert ','.join(sorted(e)) == 'fkb,nnr,rdn,rqf,rrn,z16,z31,z37'

# gcg,grr,kcm,nbm,qsj,qsj,tjk,tjk
# bss,gcg,grr,kcm,nbm,qsj,tjk,tnn
# bss,kwh,qqr,qsj,tjk,tnn,x37,y37
# bss,fkb,qsj,rcc,tjk,tnn,x37,y37


