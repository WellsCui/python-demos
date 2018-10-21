import org.wells.graphlib as graphlib


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class PositionNode:
    def __init__(self, pos: Position, data):
        self.pos = pos
        self.data = data


class MatrixGraph(graphlib.IGraph):
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_high = len(self.matrix)
        self.matrix_width = len(self.matrix[0])

    def get_adjacent_1d(self, p, scope):
        if p == 0:
            return [0, 1]
        elif p == scope - 1:
            return [p - 1, p]
        else:
            return [p - 1, p, p + 1]

    def get_adjacent_2d(self, p: Position, scope):
        row_range = self.get_adjacent_1d(p.row, scope[0])
        col_range = self.get_adjacent_1d(p.col, scope[1])
        neighbor = []
        for r in row_range:
            if r != p.row:
                neighbor.append(Position(r, p.col))
        for c in col_range:
            if c != p.col:
                neighbor.append(Position(p.row, c))
        return neighbor

    def get_links(self, node: PositionNode):
        adjacent_positions = self.get_adjacent_2d(node.pos, [self.matrix_high, self.matrix_width])
        return (PositionNode(pos, self.matrix[pos.row][pos.col]) for pos in adjacent_positions)


def matrix_graph_test():
    g = MatrixGraph([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]
                     ])
    links = g.get_links(PositionNode(Position(2, 2), g.matrix[2][2]))
    for l in links:
        print(l.data)


matrix_graph_test()
