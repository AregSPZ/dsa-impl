from vertex import Vertex

class Graph:

    def __init__(self):
        # key - a vertex key
        # value - the vertex
        self.vertices = {}

    def add_vertex(self, key):
        '''Add a vertex into graph'''
        self.vertices[key] = Vertex(key)
    
    def add_edge(self, from_vert, to_vert, weight=0):
        '''Add a new edge into the graph'''
        if from_vert not in self.vertices:
            self.add_vertex(from_vert)
        if to_vert not in self.vertices:
            self.add_vertex(to_vert)
        self.vertices[from_vert].link(to_vert, weight)

    def get_vertex(self, key):
        '''Get the vertex under a certain key''' 
        return self.vertices.get(key, None)

    def get_vertices(self):
        '''Get the keys for all the vertices'''
        return self.vertices.keys()
    
    def size(self):
        '''Get the number of vertices in graph'''
        return len(self.vertices)
    
    def __contains__(self, key):
        # 'if vertkey in Graph'
        return key in self.vertices
    
    def __iter__(self):
        # make iterable through vertices themselves
        return iter(self.vertices.values())


# example usage
if __name__ == '__main__':
    G = Graph()
    for i in range(6):
        G.add_vert(i)
    for from_, to in {0: [1,5], 1: [2], 2: [3], 3: [4,5], 4: [0], 5: [2,4]}.items():
        for to in to:
            G.add_edge(from_, to)

    for v in G:
        print(v)