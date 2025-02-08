class Vertex:
    def __init__(self, key):
        # the id of a vertex and its adjacency list
        self.key = key
        self.adj = {}

    def get_weight(self, key):
        '''Get the weight of an edge'''
        return self.adj.get(key, None)
    
    def link(self, key, weight=0):
        '''Add a new edge to the vertex'''
        self.adj[key] = weight
    
    def __repr__(self):
        return f'Vertex({self.key})'

    def __str__(self):
        return (
            str(self.key) 
            + ' connected to: '
            + str([x for x in self.adj.keys()])
        )
        
    def get_all(self):
        '''Get all the vertices linked to'''
        return self.adj.keys()
    
    def get_key(self):
        return self.key
    

# Example usage
if __name__ == "__main__":
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)

    v1.link(v2, 5)
    v1.link(v3, 10)

    print(v1)  # Output: 1 connected to [2, 3]
    print(v1.get_weight(v2))  # Output: 5
    print(v1.get_weight(v3))  # Output: 10
    print(v1.get_all())  # Output: dict_keys([2, 3])