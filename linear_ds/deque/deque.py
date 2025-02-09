class Deque:

    def __init__(self, items=[]):
        self._items = [item for item in items]

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)
    
    def remove_front(self):
        return self._items.pop()
    
    def remove_rear(self):
        return self._items.pop(0)
    
    def is_empty(self):
        return not self._items
    
    def size(self):
        return len(self._items)