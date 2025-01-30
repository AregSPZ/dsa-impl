class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        '''Add a new item to the rear'''
        self._items.insert(0, item)
    
    def dequeue(self):
        '''Remove the item at front'''
        return self._items.pop()
    
    def is_empty(self):
        return True if len(self._items) == 0 else False
    
    def size(self):
        return len(self._items)

class ReverseQueue:
    '''Rear and front are reversed'''

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        '''Add a new item to the rear'''
        self._items.append(item)
    
    def dequeue(self):
        '''Remove the item at front'''
        return self._items.pop(0)
    
    def is_empty(self):
        return True if len(self._items) == 0 else False
    
    def size(self):
        return len(self._items)
