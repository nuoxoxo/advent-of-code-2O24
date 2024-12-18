import re
up,down = open(0).read().strip().split('\n\n')
up = up.splitlines()
A,B,C = [int(_.split(': ')[1]) for _ in up]
A,down=117440,'0,3,5,4,3,0'
program = list(map(int,re.findall( r'\d+', down)))
print(A,B,C,program)

def getcombo(n) -> int:
    if n in [0,1,2,3]: return n
    if n == 4: return A
    if n == 5: return B
    if n == 6: return C
    print('n/',n)
    assert False

res = []
i = 0
#for i in range(0, len(program), 2):
while i < len(program):
    jumped = False
    code = program[i]
    oper = program[i + 1]
    combo = getcombo(oper)
    if code == 0: A //= (2 ** combo) #adv
    if code == 1: B ^= oper #bxl
    if code == 2: B = combo % 8 #bst
    if code == 3 and A != 0: i, jumped = oper, True#jnz
    if code == 4: B ^= C#bxc
    if code == 5: res.append(combo % 8) #out
    if code == 6: B = A // (2**combo) #bdv
    if code == 7: C = A // (2**combo) #cdv
    if not jumped: i += 2
    #print(res)#len(res), i, code, oper)
res = ','.join([str(_) for _ in res])
print('res/', res)
assert(res in['7,4,2,0,5,0,5,3,7','4,6,3,5,6,3,5,2,1,0','0,3,5,4,3,0'])
