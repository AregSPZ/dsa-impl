from node import Node




class UnorderedList:
    '''A linked list where the items dont follow an ordering pattern. It is assumed that the list should contain unique values'''

    def __init__(self):
        '''Initialize with no head
        The head is the list's first element'''
        # there is no head, which means the list is empty
        self.head = None
        self.tail = self.head # the variable that tracks the last item in the list (also None at the start as the list is empty). useful for making append O(1)
        self.size = 0


    def is_empty(self):
        '''Checks if the list is empty'''
        return self.head == None # which means the head isnt set

    def add(self, item):
        '''Add a new item into the beginning of the list (it becomes the new head)'''
        node = Node(item) # store the data in the node
        node.next = self.head # link the node to the current head node (basically this way the 1st value is linked to 2nd, the 2nd to 3rd etc)
        # if the item is the first one added, it will be at the very front of the list, point nowhere and its next attribute will be None
        self.head = node # set it as the new head
        # in this system all the list's items except for the last one have next attribute (link to something after them)
        # if the list was empty and this is the one and only item after adding, then its both the head and the tail of the list (also handles the append method)
        if node.next == None:
            self.tail = node
        
        self.size += 1


    def append(self, item):
        '''Add a new item to the end (tail) of the list, contrary to add() which adds the items to the head'''
        node = Node(item) # store the desired item in a node
        if not self.is_empty():
            old_tail = self.tail # get the old tail which will be replaced by this item
            old_tail.next = node # link old tail to new tail
            self.tail = node # set the new tail
            # the tail variable allowed us to make append O(1)
        # if the list is empty then just use add method as theres no difference (the last conditional is activated)
            self.size += 1
        else:
            self.add(item)

        
        

    def search(self, item):
        '''Checks if a value is contained in the list'''
        # start from the head and go right to that item
        current = self.head 
        # search until the end (going through all the items in order). the last item has no next one, which makes its next attribute None
        while current != None:
            # if we see it at some point then true
            if current.data == item:
                return True
            # the last item's next is None. at the end current becomes None if we reach no result
            current = current.next

        # if we reach the end without result then false
        return False

    def remove(self, item):
        '''Remove an item from the linked list. As it doesnt go backward here (only next one at right), we should improvize'''
        # inchworming. 2 consecutive nodes go and go close to each other. if the current one becomes the item we want to remove then we link its previous node to this item's next one, effectively leaving out the current one from the linked list 
        previous = None
        current = self.head
        # same as in search(), we go till end
        while current != None:
            # stop when we reach the desired item
            if current.data == item:
                break
            previous = current
            current = current.next
  
    
        # in case we reach the end and dont find that item
        # or the list is just empty
        if current == None:
            raise ValueError('The item specified is not contained in the list')
        
        
        # the following code assumes that the item was found.
        # the special case of removal: the item we want to remove is the head itself
        if previous == None:
            self.head = current.next # we just make the next item in the list the head
    
        # the general case of removal discussed above
        else:
            previous.next = current.next
            # set the tail to the second last node if the removed node was the tail
            if self.tail == current:
                self.tail = previous

        self.size -= 1

    def insert(self, index, item):
        '''Insert an item into the list'''

        # the index 0 case is equal to add() function
        if index == 0:
            self.add(item)

        else:
            node = Node(item)
            i = 0
            current = self.head
            # assign current to the (index-1)-th node
            while i < index - 1:
                current = current.next
                i += 1
            # get the old index-th node 
            node_next = current.next
            # link the (index-1)th node to the new node
            current.next = node
            # link the new node to the old indexth node, thus completing the insertion
            node.next = node_next


    def index(self, item):
        '''Return the position of the item in the list'''
        
        i = 0
        current = self.head
        # go through nodes
        while current != None:
            # return the value of i which represents the index we're at when faced with item
            if current.data == item:
                return i
            current = current.next
            i += 1
        # we should have found that item at this point
        raise ValueError('Item not found in list')
    

    def pop(self, pos=None):
        '''pop() like in Python list'''
        current = self.head
        # assign current to last node if no position specified
        if pos == None:
            current = self.tail 
            # set the second last node as the tail
            new_tail = self.head 
            while new_tail.next != self.tail:
                new_tail = new_tail.next
            self.tail = new_tail
        # otherwise get to specified position
        else:
            while self.index(current.data) < pos:
                current = current.next
        # remove the node from the list and return it
        self.remove(current.data)
        return current   
    
    def _slice(self, start, stop):
        '''Get a slice (copy) of the linked list'''
        if stop == -1:
            stop = self.size
        # self reference
        slice_ = UnorderedList()
        # go through instances and get the nodes at specified indices
        current = self.head
        # added the current != None as the loop would give error because it would try to get the index of a None object (the next of the tail) when you specify stop to the last node
        while current != None and self.index(current.data) < stop:
            if self.index(current.data) >= start:
                slice_.append(current.data)
            current = current.next
        return slice_
    
    def to_list(self):
        '''Convert the linked list to a python list'''
        L = []
        current = self.head
        while current != None:
            L.append(current.data)
            current = current.next
        return L
    
    def __str__(self):
        '''The list will be represented as a python list'''
        return str(self.to_list())
    


# testing
if __name__ == '__main__':
    ul = UnorderedList()

    ul.append(34)
    ul.add(13)
    ul.add(28)
    ul.remove(28)
    ul.append(12)
    ul.append(15)
    ul.remove(15)
    ul.append(15)
    ul.append(23)
    ul.append(24)
    ul.append(27)



    print(ul.pop(1))
    print(ul.size)
    print(ul.search(15))
    print(ul.tail)

    print(ul)

    ul_slice = ul._slice(0, -1)
    ul_slice_1 = ul._slice(0, 5)
    ul_slice_2 = ul._slice(0, 3)

    print(ul_slice, ul_slice_1, ul_slice_2)

    new_ul = UnorderedList()

    print(new_ul._slice(0, 2))