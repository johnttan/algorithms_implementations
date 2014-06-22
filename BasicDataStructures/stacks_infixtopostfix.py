# Converts infix notation (a+b)*c to postfix notation ab+c*

def convert(exp):
    opstack = []
    output = []
    op = {
    '*':2,
    '/':2,
    '+':1,
    '-':1
    }

    for l in exp:
        if l == '(':
            opstack.append(l)
        elif l == ')':
            while opstack[len(opstack)-1] != '(':
                output.append(opstack.pop())
            opstack.pop()
        elif l in op.keys():

            while len(opstack) > 0 and opstack[len(opstack)-1] != '(' and op[opstack[len(opstack)-1]] >= op[l]:
                output.append(opstack.pop())
            opstack.append(l)
        elif l != ' ':
            output.append(l)
    
    while len(opstack) > 0:
        output.append(opstack.pop())
    return ''.join(output)

print(convert('( A + B ) * C - ( D - E ) * ( F + G )'))