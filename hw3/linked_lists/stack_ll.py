from unordered_list import UnorderedList

class StackFromLinkedList:
    '''Implement a stack using linked lists.'''
    def __init__(self):
        self._items = UnorderedList()

    def push(self, item):
        '''Push an item into the stack'''
        self._items.append(item)

    def pop(self):
        '''Pop an item from the stack'''
        return self._items.pop()
    
    def peek(self):
        '''Peek at the top of the stack'''
        return self._items.tail
    
    def is_empty(self):
        '''Check if the stack is empty'''
        return self._items.size == 0
    
    def size(self):
        '''Get the number of items in the stack'''
        return self._items.is_empty()
    


# testing
if __name__ == '__main__':
    s = StackFromLinkedList()

    for _ in [s.is_empty(), s.push(4), s.push('dog'), s.peek(), s.push(True), s.size(), s.is_empty(), s.push(8.4), s.pop(), s.pop(), s.size()]:

        print(_)