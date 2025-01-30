from unordered_list import UnorderedList

class DequeFromLinkedList:

    def __init__(self):
        self._items = UnorderedList()

    def add_rear(self, item):
        self._items.insert(0, item)

    def add_front(self, item):
        self._items.append(item)
    
    def remove_rear(self):
        return self._items.pop(0)

    def remove_front(self):
        return self._items.pop()
    
    def is_empty(self):
        return self._items.is_empty()
    
    def size(self):
        return self._items.size