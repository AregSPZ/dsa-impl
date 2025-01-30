class Stack:

    def __init__(self):
        '''Initialize a list that stores the elements of the stack'''
        self._items = []

    def push(self, item):
        '''Push an item into stack'''
        self._items.append(item)

    def pop(self):
        ''''Take and return the last pushed element from stack'''
        return self._items.pop()
    
    def peek(self):
        '''Same as pop but the element stays in the stack'''
        return self._items[-1]
    
    def is_empty(self):
        '''Checks if the stack is empty'''
        return True if len(self._items) == 0 else False
    
    def size(self):
        '''Returns the number of items in the stack'''
        return len(self._items)

