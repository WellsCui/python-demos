"""
Clone a linked list with next and random pointer | Set 1
You are given a Double Link List with one pointer of each node pointing to the next node just like in a single link list. The second pointer however CAN point to any node in the list and not just the previous node. Now write a program in O(n) time to duplicate this list. That is, write a program which will create a copy of this list.

Let us call the second pointer as arbit pointer as it can point to any arbitrary node in the linked list.


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None

class Solution:

    def __init__(self):
        self.copied_nodes = {}

    def deep_copy(self, node):
        if node is None:
            return None
        if node in self.copied_nodes:
            return self.copied_nodes[node]

        copy = Node(node.data)
        self.copied_nodes[node] = copy
        copy.next = self.deep_copy(node.next)
        copy.arbit = self.deep_copy(node.arbit)
        return copy


def test_solution():
    def build_test_node():
        data = [(1, (2, 3)), (2, (3, None)), (3, (4, 8)),
                 (4, (5, 1)), (5, (6, 2)), (6, (7, 4)),
                 (7, (8, None)), (8, (9, 2)), (9, (None, 7))]

        nodes = {}

        for (d, _) in data:
            nodes[d] = Node(d)
        for (d, (nxt, arbit)) in data:
            if nxt is not None:
                nodes[d].next = nodes[nxt]
            if arbit is not None:
                nodes[d].arbit = nodes[arbit]

        return nodes[1]

    def get_node_data(nd):
        if nd is not None:
            return nd.data

    def print_node(nd):
        print("data: %s, next: %s, arbit: %s" %
              (nd.data, get_node_data(nd.next), get_node_data(nd.arbit)))

    copy = Solution().deep_copy(build_test_node())

    while copy:
        print_node(copy)
        copy = copy.next

test_solution()










