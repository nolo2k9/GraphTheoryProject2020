
'''Keith Nolan '''
'''Classes used in thompsons construction'''


class State:

    '''Every state has 0,1 or 2 edges from it'''
    edges = []

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

    def __init__(self, start, accept):
        self.start = start
        self.accept = accept


def shunt(infix):
    # Convert input to a stack-ish list
    infix = list(infix)[::-1]

    # Operator
    op_stack = []

    # Output list
    postfix = []

    '''
 Operartor precedence
 *-1
 .-2
 |-3
 '''
    prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

    # loop through input one character at a time
    while infix:
        '''Decide what to do based on character '''
        c = infix.pop()
        if c == '(':
            """Push an open bracket to the op_stack"""
            op_stack.append(c)
        elif c == ')':
            '''Pop the operators stack until you find an open bracket ('''
            while op_stack[-1] != '(':
                postfix.append(op_stack.pop())
            ''' Get rid of the '(' '''
            op_stack.pop()
        # if c is contained in prec
        elif c in prec:
            ''' Push any operators on the opers stack with higher precedence to the output'''
            while op_stack and prec[c] < prec[op_stack[-1]]:
                postfix.append(op_stack.pop())

            op_stack.append(c)
        # else if its someting else
        else:
            postfix.append(c)

    # pop all operators to the output
        while op_stack:
            postfix.append(op_stack.pop())

    # Convert output list to String
    return ''.join(postfix)


def compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        '''Pop a character from post fix'''
        c = postfix.pop()
        if c == '.':
            '''pop 2 fragments off the stack '''
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            '''Point frag2's accept state at frag1's start state'''
            frag2.accept.edges.append(frag1.start)
            '''Create a new instance of Fragment to represent the new NFA'''
            newfrag = Fragment(frag2.start, frag1.accept)
            '''Push the new nfa to the nfa stack'''
            
        elif c == '|':
            '''Pop 2 Fragments off the stack'''
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            '''Create new start and accept states'''
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            '''Point the old accept state at the new one'''
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            newfrag = Fragment(start, accept)
            

        elif c == '*':
            '''Pop a single fragment off the stack'''
            frag = nfa_stack.pop()
            '''Create new start and accept states'''
            accept = State()
            '''point the arrows'''
            start = State(edges=[frag.start, accept])
            frag.accept.edges = [frag.start, accept]
            '''Create new instance of the fragment'''
            newfrag = Fragment(start, accept)
           

        else:
            accept = State()
            start = State(label=c, edges=[accept])
            newfrag = Fragment(start, accept)
            '''Push new nfa to the stack'''
            nfa_stack.append(newfrag)

        '''
        The nfa stack shoul have exactly 1 nfa on it
        '''
        return nfa_stack.pop()

# Add a state to a set and follow all of the e(psilon) arrows


def follows(state, current):
    # only do something when we haven't already seen the state
    if state not in current:
        # Put actual state into current
        current.add(state)
        # See whether state is labeled by e(psilon)
        if state.label is None:
            # Loop through the states pointed to by this state
            for x in state.edges:

                # follow all of their e(psilon)s too
                follows(x, current)


'''
 This function takes in a regular expression and checks to see whether it matchs a string(s) if it matchs it will return (true) otherwise it will return a false
'''
def match(regular_ex, s):
    '''
    nfa = non deterministic finite automoton
    compile
    will give us the nfa that does what the regular expression is meant to do
    '''
    nfa = compile(regular_ex)

    # Try to match the regular expression with the string s
    '''
     current = current set of states we are in
     contains the start state of the nfa
     '''
    current = set()
    '''Add the first state, and follow all e(psilon) arrows'''
    follows(nfa.start, current)

    # Previous set of states
    previous = set()

    # loop through characters in s
    for c in s:
        '''Keep track of where we were'''
        previous = current
        '''Create a new empty set for states we are about to be in'''
        current = set()

        # Loop through each of the elements in the set of  previous states
        for state in previous:
            # Only follow arrows not labeled by e(psilon)
            if state.label is not None:
                # If the label of the state is equal to the character read:
                if state.label == c:
                   
                    # Add the state at the end of the arrow to current
                    follows(state.edges[0], current)

    '''will tell us if the nfa matchs the string '''
    return nfa.accept in current


print(match("a.b|b*", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
