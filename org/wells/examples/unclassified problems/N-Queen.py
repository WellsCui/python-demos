# place n queens in n*n board
class Location:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class NQueenProblem:
    def __init__(self, n):
        self.n = n;

    def check_two_queen(self, loc1, loc2):
        if loc1.col == loc2.col or loc1.row == loc2.row:
            return True
        elif abs(loc1.col - loc2.col) == 1 and abs(loc1.row - loc2.row) == 1:
            return True
        else:
            return False

    def validate_location(self, loc, located_queens):
        for queen in located_queens:
            if self.check_two_queen(queen, loc):
                return False
        return True

    def find_unlocated(self, located):
        return [i for i in range(self.n) if i not in located]

    def try_with_located_queens(self, located_queens):
        print("trying_with %d queens located" % len(located_queens))
        for loc in located_queens:
            print("located_queen  col: %s, row: %s" % (loc.row, loc.col))
        if len(located_queens) == self.n:
            return located_queens

        rows = self.find_unlocated([loc.row for loc in located_queens])
        cols = self.find_unlocated([loc.col for loc in located_queens])

        for row in rows:
            for col in cols:
                loc = Location(row, col)
                if self.validate_location(loc, located_queens):
                    result = self.try_with_located_queens(located_queens + [loc])
                    if result:
                        return located_queens
        return None

    def solve(self):
        return self.try_with_located_queens([])

# def place_queens(n):
#     rows = [i for i in range(n)]
#     cols = [i for i in range(n)]
#     located_queens = []
#
#     def check_two_queen(loc1, loc2):
#         if loc1.col == loc2.col or loc1.row == loc2.row:
#             return True
#         elif abs(loc1.col - loc2.col) == 1 and abs(loc1.row - loc2.row) == 1:
#             return True
#         else:
#             return False
#
#     def validate_location(loc):
#         for queen in located_queens:
#             if check_two_queen(queen, loc):
#                 return False
#         return True
#
#     def find_location():
#         for r in rows:
#             for c in cols:
#                 loc = Location(r, c)
#                 if validate_location(loc):
#                     return loc
#         return None
#
#     for queen_i in range(n):
#         new_loc = find_location()
#         if new_loc:
#             located_queens.append(new_loc)
#             rows.remove(new_loc.row)
#             cols.remove(new_loc.col)
#     return located_queens
#
#
# def place_queens_test():
#     queens = place_queens(8)
#     for q in queens:
#         print("col: %s, row: %s" % (q.row, q.col))


def n_queen_problem_test():
    locations = NQueenProblem(8).solve()
    for loc in locations:
        print("col: %s, row: %s" % (loc.row, loc.col))

n_queen_problem_test()




