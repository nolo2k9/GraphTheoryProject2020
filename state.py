
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



class Frag:
    '''Start State of NFA fragment '''
    start = None
    '''Accept state of NFA Fragment'''
    accept = None

    '''Constructor for class'''
    def __init__(self,start,accept):
        self.start = start
        self.accept = accept


my_instance = State(label='a', edges=[])
my_other_instance = State(edges=[my_instance])
my_fragment = Frag(my_instance, my_other_instance)
print(my_instance.label)
print(my_other_instance.edges[0])
print(my_fragment)
