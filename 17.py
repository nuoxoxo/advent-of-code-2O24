import re
up,down = open(0).read().strip().split('\n\n')
up = up.splitlines()
a,b,c = [int(_.split(': ')[1]) for _ in up]
program = list(map(int,re.findall( r'\d+', down)))

def gc(n,a,b,c) -> int:
        if n in [0,1,2,3]: return n
        if n == 4: return a
        if n == 5: return b
        if n == 6: return c

# p2/ 16312849068642 lo 

def p2(curr, sub):
    if sub == []: return curr
    N = len(program)
    #print(sub)
    for digit in range(8):
        #print(digit)
        a = curr << 3 | digit
        b, c = 0, 0
        o = None
        for i in range(0, len( program ) - 2, 2):
            code = program [i]
            oper = program [i + 1]
            combo = gc (oper,a,b,c)
            # opcode is never 0 bc. in reverse A grows and should not shrink
            #   except when operand is 3
            #   even in this case we do nothing
            #if code == 0 and oper != 3: a >>= combo #adv
            if code == 1: b ^= oper #bxl
            if code == 2: b = combo % 8 #bst
            if code == 3 and a != 0: i, jumped = oper, True#jnz
            if code == 4: b ^= c#bxc
            if code == 5: o = combo % 8 # res.append(combo % 8) #out
            if code == 6: b = a >> combo# // (2**combo) #bdv
            if code == 7: c = a >> combo# // (2**combo) #cdv
            if o == sub[-1]:
                recur = p2(a, sub[:-1])
                if recur is not None:
                    return recur

"""p2 : logic
# 2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0
#   2 4/ bst
#       b = getcombo(4) % 8 = a % 8
#       b = a % 8
#   1 1/ bxl
#       b = b ^ oper ---> (a % 8) ^ 1 = 0
#       b = 0
#   7 5/ cdv
#       c = a >> gc(5) = a >> b = a >> 0 = a
#       c = a
#   4 4/ bxc
#       b = b ^ c = b ^ a = 0 XOR a = a
#       b = a
#   1 4/ bxl
#       b = b ^ 4 = a ^ 4
#   0 3/ adv
#       a = a >> combo = a >> gc(3) = a >> 3
#   5 5/ out
#       out gc(5) % 8 = a ^ 4 % 8
#   3 0/ jnz
#       if a != 0: i = back to the beginning

#       summary/
#   b = a % 8
#   b = (a % 8) ^ 1 --- flip each bit of it
#   c = a >> (a % 8)
#   b = (a % 8) ^ (a >> b)
#   b = (a % 8) ^ 4
#   next_a = prev_a >> 3
#   out/ prev_a % 8
#   if a != 0: i = 0
"""

def getcombo(n) -> int:
    if n in [0,1,2,3]: return n
    if n == 4: return a
    if n == 5: return b
    if n == 6: return c
    print('n/',n)
    assert False

#a,down=117440,'0,3,5,4,3,0' # try p2test input for p1

res = []
i = 0
while i < len(program):
    jumped = False
    code = program[i]
    oper = program[i + 1]
    combo = getcombo(oper)
    if code == 0: a >>= combo # //= (2 ** combo) #adv
    if code == 1: b ^= oper #bxl
    if code == 2: b = combo % 8 #bst
    if code == 3 and a != 0: i, jumped = oper, True#jnz
    if code == 4: b ^= c#bxc
    if code == 5: res.append(combo % 8) #out
    if code == 6: b = a >> combo # // (2**combo) #bdv
    if code == 7: c = a >> combo # // (2**combo) #cdv
    if not jumped: i += 2

res = ','.join([str(_) for _ in res])
print('part 1/', res)
assert(res in['7,4,2,0,5,0,5,3,7','4,6,3,5,6,3,5,2,1,0','0,3,5,4,3,0'])
res2 = p2(0, program)
print('part 2/', res2)