from unordered_list import UnorderedList

class DequeLL:

    def __init__(self, items=[]):
        self._items = UnorderedList()
        for item in items:
            self._items.append(item)

    def addrear(self, item):
        self._items.insert(0, item)

    def append(self, item):
        self._items.append(item)
    
    def poprear(self):
        return self._items.pop(0)

    def pop(self):
        return self._items.pop()
    
    def is_empty(self):
        return self._items.is_empty()
    
    def size(self):
        return self._items.size