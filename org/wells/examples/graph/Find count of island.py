# A group of connected 1s forms an island now your task is to complete the method findIslands which
#  returns the no of islands present. The function  takes three arguments the first is the boolean
#  matrix A and then the next two arguments are N and M denoting the size of the matrix A .

class Location:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def is_adjacent(self, loc):
        return abs(loc.row - self.row) < 2 and abs(loc.col - self.col) < 2

    def __str__(self):
        return str.format("(%d, %d)" % (self.row, self.col))

class Island:
    def __init__(self, loc):
        self.locs = [loc]

    def is_connected(self, island):
        for loc1 in self.locs:
            for loc2 in island.locs:
                if loc1.is_adjacent(loc2):
                    return True
        return False

    def merge(self, island):
        self.locs += island.locs

    def __str__(self):
        return str.join(", ", [loc.__str__() for loc in self.locs])

class BooleanMatrixIslandFinder:

    def __init__(self, matrix):
        self.matrix = matrix

    def join_islands(self, island, islands):
        for dst in islands:
            if dst.is_connected(island):
                dst.merge(island)
                return islands
        return islands + [island]

    def merge_islands(self, islands):
        islands_num = len(islands)
        if islands_num < 2:
            return islands
        merged_islands = []
        while islands:
            merged_islands = self.join_islands(islands.pop(), merged_islands)
        if len(merged_islands) == islands_num:
            return merged_islands
        else:
            return self.merge_islands(merged_islands)

    def find_islands(self):
        islands = []
        for row_index, row in enumerate(self.matrix):
            for col_index, data in enumerate(row):
                if data==1:
                    islands.append(Island(Location(row_index, col_index)))
        return self.merge_islands(islands)


def test_island_finder():
    matrix = [[1, 0, 1, 0, 0, 1, 0, 1],
              [1, 1, 1, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [1, 1, 1, 0, 0, 1, 1, 1],
              [0, 0, 1, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 1, 1, 0, 1],
              [0, 0, 1, 0, 1, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 1, 1]]

    islands = BooleanMatrixIslandFinder(matrix).find_islands()
    print("found %d" % len(islands))
    for island in islands:
        print(island)

test_island_finder()


