from graph import Graph
from collections import deque

def bfs(G, s, k=float('inf')):
    '''G - the graph
       s - the starting vertex key
       k - how much levels to explore: if not specified process the whole graph'''
    # initialize the colors to white (unprocessed)
    # except from the starting one
    color = {s: 'grey'}
    for vertex in G:
        color[vertex.get_key()] = 'white'
    # gray - processed itself but has adjacent white nodes
    # black - fully processed
    i = 0
    # start from the starting node
    queue = deque([G.get_vertex(s)])
    while queue and i < k:
        # extract the first in queue
        node = queue.popleft()
        # enqueue its neigbors and label them as grey
        for neigh in node.get_all():
            # avoid processing the node if it was already visited
            if color[neigh] == 'white':
                print(neigh)
                color[neigh] = 'grey'
                queue.append(G.get_vertex(neigh))
        # label the current node as black as we went through all of its neighbors
        color[node] = 'black'
        i += 1
        

if __name__ == "__main__":
    # Create a graph instance
    G = Graph()
    
    # Add vertices
    for i in range(6):
        G.add_vertex(i)
    
    # Add edges
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    
    # Perform BFS
    bfs(G, 0)
    
    # Perform BFS with level limit
    bfs(G, 0, 2)