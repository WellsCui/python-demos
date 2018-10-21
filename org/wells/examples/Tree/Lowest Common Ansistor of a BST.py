class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LowestCommonAncestorFinder:

    def findAncestor(self, parent, sbtNode, data):
        if sbtNode is None:
            return parent
        elif sbtNode.data == data:
            return parent
        elif data > sbtNode.data:
            return self.findAncestor(sbtNode, sbtNode.right, data)
        else:
            return self.findAncestor(sbtNode, sbtNode.left, data)

    def find_ancestor(self, parent, sbtNode, bigger, smaller):
        print(sbtNode.data)
        if sbtNode is None:
            return None
        if sbtNode.data == bigger or sbtNode.data == smaller:
            return parent
        elif bigger > sbtNode.data > smaller:
            return sbtNode
        elif bigger < sbtNode.data:
            return self.find_ancestor(sbtNode, sbtNode.left, bigger, smaller)
        else:
            return self.find_ancestor(sbtNode, sbtNode.right, bigger, smaller)

    def find(self, sbtRoot, data1, data2):
        if data1 > data2:
            return self.find_ancestor(None, sbtRoot, data1, data2)
        # elif data1 < data2:
        else:
            return self.find_ancestor(None, sbtRoot, data2, data1)
        # else:
        #     return self.findAncestor(None, sbtRoot, data1)

def build_sbt():
    root = Node(25)
    root.left = Node(11)
    root.right = Node(43)
    root.left.left = Node(5)
    root.left.right = Node(17)
    root.left.left.left = Node(3)
    root.left.left.right = Node(6)
    root.left.right.left = Node(13)
    root.left.right.right = Node(23)
    root.right.left = Node(33)
    root.right.left.left = Node(29)
    root.right.left.right = Node(43)
    root.right.right = Node(51)
    root.right.right.left = Node(43)
    root.right.right.right = Node(53)
    return root

def test_finder():
    print(LowestCommonAncestorFinder().find(build_sbt(), 25, 29).data)

test_finder()
