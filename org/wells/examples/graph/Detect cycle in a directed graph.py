# Given a directed graph  your task is to complete the method isCycle
# to detect if there is a cycle in the graph or not.
__
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.links = []

class GraphCycleDetector:

    def check_node_with_path(self, node, path):
        if node in path:
            return False
        for link in node.links:
            if not self.check_node_with_path(link, path + [node]):
                return False
        return True


    def check_node(self, node):
        return self.check_node_with_path(node, [])


