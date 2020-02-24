
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

def regular_ex_compile(regular_ex):




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


