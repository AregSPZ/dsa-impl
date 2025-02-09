from pythonds3.graphs import Graph

def gen_legal_moves(i, j, board_size):
    '''Generate legal moves for each cell on chessboard'''
    new_moves = []
    directions = [
        (-1, -2),  # left-down-down
        (-1, 2),   # left-up-up
        (-2, -1),  # left-left-down
        (-2, 1),   # left-left-up
        (1, -2),   # right-down-down
        (1, 2),    # right-up-up
        (2, -1),   # right-right-down
        (2, 1),    # right-right-up
    ]
    # add the move if its within borders
    for di, dj in directions:
        if 0 <= i + di < board_size and 0 <= j + dj < board_size:
            new_moves.append((i + di, j + dj))
    return new_moves

def knight_graph(board_size):
    '''Generate the graph representation of the Knight's tour'''
    kt_graph = Graph()
    # for each cell on chessboard
    for i in range(board_size):
        for j in range(board_size):
            node_id = i * board_size + j
            # get its legal moves
            new_positions = gen_legal_moves(i, j, board_size)
            # link the cell with its legal moves
            for i2, j2 in new_positions:
                other_node_id = i2 * board_size + j2
                kt_graph.add_edge(node_id, other_node_id)
    return kt_graph


def knight_tour(n, path, u, limit):
    u.color = "gray"
    path.append(u)
    if n < limit:
        neighbors = sorted(list(u.get_neighbors()))
        i = 0
        done = False
        while i < len(neighbors) and not done:
            if neighbors[i].color == "white":
                done = knight_tour(n + 1, path, neighbors[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.color = "white"
    else:
        done = True
    return done

KG = knight_graph(8)
print(knight_tour(0, [], KG.get_vertex(0), 64))