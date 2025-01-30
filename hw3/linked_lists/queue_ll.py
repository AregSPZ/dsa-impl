from node import Node
from unordered_list import UnorderedList

class QueueFromLinkedList:
    '''Queue implementation using a Linked Unordered List'''
# enqueue, dequeue, is_empty, size
    def __init__(self):
        self._items = UnorderedList()

    def enqueue(self, item):
        '''Insert an item into the queue'''
        self._items.add(item)

    def dequeue(self):
        '''Dequeue an item from the front of the queue'''
        return self._items.pop()
    
    def is_empty(self):
        '''Check if the queue is empty'''
        return self._items.is_empty()
    
    def size(self):
        '''Get the number of items in the queue'''
        return self._items.size
    
class QueueO1:
    '''Queue implementation with O(1) enqueue and dequeue operations
    The key here is that the front is at the start of the list while rear is at the end'''

    def __init__(self):
        '''Initialize without rear and front'''
        self.front = None
        self.rear = None

    def is_empty(self):
        '''Check if the queue is empty'''
        return self.front is None

    def enqueue(self, item):
        '''Insert an item into the queue'''
        new_node = Node(item)
        # if the queue is empty then assign both front and rear to this item
        if self.rear is None:
            self.front = self.rear = new_node
        # otherwise (there's a front) make the queue (tail) longer by linking the old rear to the new rear (this item) from the right
        # its important to understand: the queue starts from the left, which lets us utilize the next attribute of the node to point to the node which will be the next one in the front
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        '''Dequeue an item from the front of the queue'''
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        # extract the front node and assign the second one as the new front one. thus we remove the item from the list like in remove() and replace it with the next one 
        temp = self.front
        self.front = temp.next
        # if there's only 1 item in the queue (theres no one after the front one) assign rear to None so reset the queue's state
        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        '''Get the number of items in the queue'''
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

# Testing
if __name__ == '__main__':
    q = QueueO1()
    print(q.is_empty())     # True
    q.enqueue(4)
    q.enqueue('dog')
    print(q.dequeue())      # 4
    print(q.size())         # 1