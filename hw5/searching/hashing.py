class HashTable:
    '''A hash table implementation with string keys'''

    def __init__(self):
        self.table_size = 11
        # initialize the empty slots
        self.keys = [None] * self.table_size
        self.values = [None] * self.table_size

    def put(self, key, value):
        '''Put a new item into the hash table'''

        slot = self.hash_function(key)
        # if the slot is empty
        if not self.keys[slot]: 
            self.keys[slot] = key
            self.values[slot] = value

        else:
            # linear probing
            moving_slot = slot + 1
            while moving_slot != slot:

                if not self.keys[moving_slot]:
                    self.keys[moving_slot] = key
                    self.values[moving_slot] = value
                    break

                moving_slot += 1
                # go back to start
                if moving_slot > self.table_size - 1:
                    moving_slot = 0
            
            if moving_slot == slot:
                return f'Error: ({key}:{value}) couldnt be added as the table is full'
      
    
    def get(self, key):
        '''Get the value under a certain key'''

        slot = self.hash_function(key)

        if not self.keys[slot]:
            return f"Error: '{key}' not present in table"
        
        return self.values[slot]


    def hash_function(self, key):
        '''Determining the slot for the item'''
        # weighted sum if the key is a string
        if isinstance(key, str):
            ords = [ord(s) for s in key]
            # compute the weighted sum
            sum_ = 0
            for i in range(len(ords)):
                sum_ += ords[i] * (i+1)
            return sum_ % self.table_size

        # simple remainder method if an integer
        else:
            return key % self.table_size

    
    def remove(self, key):
        '''Remove the key-value pair from the table'''
        pass

    def search(self, key):
        '''Search for a key in the table'''
        pass

    def size(self):
        '''Return the number of busy slots'''
        return len([i for i in self.keys if i])

    
    # dict like functionality
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)




if __name__ == '__main__':

    table = HashTable()

    table[2] = 3

    table['catttt'] = 'vor'

    print(table['catttt'])
    print(table.size())
