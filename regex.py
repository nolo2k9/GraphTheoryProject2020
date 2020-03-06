#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Keith Nolan

# === classes ===

'''Classes used in thompsons construction'''


class State:

    '''Every state has 0,1 or 2 edges from it'''

    edges = []
    label = None

    def __init__(self, edges=[], label=None):
        self.edges = edges
        self.label = label


class Fragment:

    '''Start State of NFA fragment '''

    start = None
    accept = None

    # Constructor for class

    def __init__(self, start, accept):
        self.start = start

        self.accept = accept


# ====== Functions ==========

# convert infix to postfix

def shunt(infix):

    # convert input to list

    infix = list(infix)[::-1]

    # operator list

    op_stack = []

    # output list

    postfix = []

    prec = {
        '*': 100,
        '.': 80,
        '|': 60,
        ')': 40,
        '(': 20,
        }

    # loop through input one character at a time

    while infix:
        c = infix.pop()

        # decide logic based on character

        if c == '(':

            op_stack.append(c)
        elif c == ')':

            # pop op_stackory stack until we find an opening bracket

            while op_stack[-1] != '(':
                postfix.append(op_stack.pop())
            op_stack.pop()
        elif c in prec:

       # if c is contained in prec

            while op_stack and prec[c] < prec[op_stack[-1]]:
                postfix.append(op_stack.pop())

            # if c is an operator or bracket

            op_stack.append(c)
        else:

             # else if its someting else
            # add to postfix

            postfix.append(c)

    # pop all operators to output

    while op_stack:
        postfix.append(op_stack.pop())

    # convert output list to string

    return ''.join(postfix)


def compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:

        # pop character from postfix

        c = postfix.pop()
        if c == '.':
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()

            # point frag2's accept state to frag1 start state

            frag2.accept.edges.append(frag1.start)

            newFrag = Fragment(frag2.start, frag1.accept)
        elif c == '|':

            # pop 2 fragments off the stack

            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()

            # create new start and accept states

            accept = State()
            start = State(edges=[frag2.start, frag1.start])

            # point old accept state to new one

            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)

            # new instance of fragment to represent NFA

            newFrag = Fragment(start, accept)
        elif c == '*':

            # pop a single fragment off the stack

            frag = nfa_stack.pop()

            # create a new start and accept states

            accept = State()
            start = State(edges=[frag.start, accept])

            # point the arrows

            frag.accept.edges = [frag.start, accept]

            # create a new instance of Fragment to represent NFA

            newFrag = Fragment(start, accept)
        else:

            accept = State()
            start = State(label=c, edges=[accept])

            newFrag = Fragment(start, accept)

        nfa_stack.append(newFrag)

    return nfa_stack.pop()


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


def match(regular_ex, s):
    '''
    nfa = non deterministic finite automoton
    compile
    will give us the nfa that does what the regular expression is meant to do
    '''

    nfa = compile(regular_ex)

    # Try to match the regular expression with the string s

    current = set()
    follows(nfa.start, current)

    # Previous set of states

    previous = set()

    # loop through characters in s

    for c in s:
        previous = current
        current = set()

        # Loop through each of the elements in the set of  previous states

        for state in previous:

            # Only follow arrows not labeled by e(psilon)

            if state.label is not None:

                # If the label of the state is equal to the character read:

                if state.label == c:

                    # Add the state at the end of the arrow to current

                    follows(state.edges[0], current)

    return nfa.accept in current


print (match("a.b|b*", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))


			