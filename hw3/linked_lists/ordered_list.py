from node import Node
from unordered_list import UnorderedList

class OrderedList:
    '''A linked list where the items follow an ordering pattern (in this case ascending order) 
    Ordered Linked Lists share some of its functionality with Unordered Linked Lists
    In my implementation, Ordered List doesn't provide a tail attribute unlike the Unordered List as it doesnt have an append method'''
    
    def __init__(self):
        # most of the methods will use the functionality of unordered lists under the hood
        self.ul = UnorderedList()
        self.head = None


    def add(self, item):
        '''Add a new node to the list'''
        node = Node(item)
        # if the list is empty then we can just assign the node to the head
        if self.is_empty():
            node.next = self.head
            self.head = node
        # if its not then we do inchworming (traversing) until we reach the place where we shoold place the new node
        else:
            previous = None
            current = self.head
            while current != None:
                if current.data > node.data:
                    break
                previous = current
                current = current.next

            # link the node to current from right
            node.next = current   
            # if previous is none then node is the head (theres no item from the left of the node)
            if previous == None:
                self.head = node
            # otherwise link the node to the previous node from left
            else:
                previous.next = node
                 

        # add the item to the base unordered list so we can use its is_empty and size and get an identical resolt
        self.ul.add(item)
        

    def search(self, item):
        '''Search for an item in the list
           Returns a boolean value'''
        # start from the head and traverse
        current = self.head
        while current != None:
            # if the node's value is bigger we can just stop prematurely
            if current.data > item:
                return False
            # elseif its equal then we found the node
            elif current.data == item:
                return True 
            # if its smaller then keep going
            current = current.next
        # if we reach the end without resolt then false
        return False

   
    def remove(self, item):
        '''Remove an item from the node'''
        previous = None
        current = self.head
        # pass through all nodes
        while current != None:
            # if we pass that value raise the error (ending prematurely considering the nature of the ordered list)
            if current.data > item:
                raise ValueError('The item specified is not contained in the list')
            elif current.data == item:
                break
            previous = current
            current = current.next

        # if we got to end with no resolt or the list is empty then raise the error
        if current == None:
            raise ValueError('The item specified is not contained in the list')

        # assume the item was found at this point
        # if the item to be removed is the head then assign the head to the second node
        if previous == None:
            self.head = current.next

        # general case of removal
        else:
            previous.next = current.next
        
        # remove in unordered list to keep track of the size of the list
        self.ul.remove(item)
        
    def index(self, item):
        '''Get the index of an item'''  
        i = 0
        current = self.head
        while current != None:
            # the same condition as in remove()
            if current.data > item:
                raise ValueError('The item specified is not contained in the list')
            elif current.data == item:
                return i
            current = current.next
            i += 1
        
        # if the loop ended without returning 'i' raise an error
        # this means that the item was bigger than all of the list's items
        raise ValueError('The item specified is not contained in the list')

    def pop(self, pos=None):
        '''pop() like in a Python list'''
        current = self.head
        # if no value specified then pop the last one in the list
        if pos == None:
            while current.next != None:
                current = current.next
        # otherwise pop at the specified index
        else:
            while self.index(current.data) < pos: 
                current = current.next
        self.remove(current.data)
        return current


    def is_empty(self):
        '''Check if the list is empty'''
        return self.ul.is_empty()
    

    def size(self):
        '''Get the number of items in the list'''
        return self.ul.size
    
    size = property(size)


    def to_list(self):
        '''Convert the linked list to a python list'''
        L = []
        current = self.head
        while current != None:
            L.append(current.data)
            current = current.next
        return L
    

# testing
if __name__ == '__main__':
    
    ol = OrderedList()

    ol.add(13)
    ol.add(28)
    ol.remove(28)
    ol.add(2)

    print(ol.pop())
    print(ol.size)
    print(ol.search(15))
    print(ol.index(2))

    ol.remove(2)
    print(ol.is_empty())

    print(ol.to_list())