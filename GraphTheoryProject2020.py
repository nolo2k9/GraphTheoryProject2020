#Keith Nolan
#The shunting yard algorithm for regular expressions

# Input
infix = "(a|b).c*"
print("Input is: ", infix)
#Expected output: ab|c*.
print("Expected: ", "ab|c*.")

#Convert input to a stack-ish list
infix = list(infix)[::-1]

#Operator
op_stack = []

#Output list
postfix = []

'''
Operartor precedence
*-1
.-2
|-3
'''
prec = {'*':100, '.':80, '|':60, ')':40, '(':20}

#loop through input one character at a time
while infix:
    '''Decide what to do based on character '''
    c = infix.pop()
    if c =='(':
        """Push an open bracket to the op_stack"""
        op_stack.append(c)
    elif c ==')':
        '''Pop the operators stack until you find an open bracket ('''
        while op_stack[-1] != '(':
             postfix.append(op_stack.pop())
        ''' Get rid of the '(' '''
        op_stack.pop()
    #if c is contained in prec
    elif c in prec:
        ''' Push any operators on the opers stack with higher precedence to the output'''
        while op_stack and  prec[c] < prec[op_stack[-1]]:
            postfix.append(op_stack.push())

        op_stack.append(c)
    #else if its someting else 
    else:
         postfix.append(c)

#pop all operators to the output        
while op_stack:
    postfix.append(op_stack.pop())



#Convert output list to String 
postfix = ''.join(postfix)

#print the result 
print("Output is:", postfix)

