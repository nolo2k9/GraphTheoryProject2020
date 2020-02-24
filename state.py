
'''Keith Nolan '''
'''Classes used in thompsons construction'''

class State:

    '''Every state has 0,1 or 2 edges from it'''
    edges =[]

    '''Label for the arrows. None means epsilon'''
    label = None

    '''Constructor for class'''
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label



class Fragment:
    '''Start State of NFA fragment '''
    start = None
    '''Accept state of NFA Fragment'''
    accept = None

    '''Constructor for class'''
    def __init__(self,start,accept):
        self.start = start
        self.accept = accept
def shunt(infix):
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
 return ''.join(postfix)

def regular_ex_compile(infix):
    postfix= shunt(infix)
    postfix =list(postfix)[::-1]

    nfa_stack = []


    while postfix:
        '''Pop a character from post fix'''
        c=postfix.pop()
        if c=='.':
            '''pop 2 fragments off the stack '''
            frag1= nfa_stack.pop()
            frag2 = nfa_stack.pop()
            '''Point frag2's accept state at frag1's start state'''
            frag2.edges.append(frag1.start)
            '''Create a new instance of Fragment to represent the new NFA'''
            newfrag = Fragment(frag2.start, frag1.accept)
            '''Push the new nfa to the nfa stack'''
            nfa_stack.append(newfrag)
        elif c =='|':
            '''Pop 2 Fragments off the stack'''
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            '''Create new start and accept states'''
            accept = State()
            start = State(edges=[frag2.start, frag1.start])


        elif c == '*':

        else:
          accept= State()
          start = State(label=c, edges=[accept])
          newfrag= Fragment(start,accept)
          nfa_stack.append(newfrag)
          
'''
 This function takes in a regular expression and checks to see whether it matchs a string(s) if it matchs it will return (true) otherwise it will return a false
'''
def match(regular_ex, s):
     '''
     nfa = non deterministic finite automoton
     regular_ex_compile will give us the nfa that does what the regular expression is meant to do
     '''
     nfa = regular_ex_compile(regular_ex)
    '''will tell us if the nfa matchs the string'''
    return nfa.match(s)
match("a.b|b*","bbbbbbbbbbb")
