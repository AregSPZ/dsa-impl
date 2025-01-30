class Node:

    def __init__(self, node_data):
        '''Initialize the node, the building block of a linked list, with the data it stores and its placement relative to other nodes (the next one)'''
        self._data = node_data
        self._next = None # not linked to anything or anyone at first

    def get_data(self):
        '''Return the data the node stores'''
        return self._data
    
    def set_data(self, node_data):
        '''Change the data the node stores'''
        self._data = node_data

    # with this we can directly access/modify the node's self.data attribute and it will call get_data and set_data respectively
    data = property(get_data, set_data)

    def get_next(self):
        '''Return the next node this one is linked to'''
        return self._next
    
    def set_next(self, next_):
        '''Change the next node this one is linked to'''
        self._next = next_

    
    # same thing here
    next = property(get_next, set_next)

    def __str__(self):
        '''Readable format for a node'''
        return str(self._data)
    