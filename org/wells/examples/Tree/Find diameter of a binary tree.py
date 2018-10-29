# Diameter of a Binary Tree
# The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between
# two end nodes. The diagram below shows two trees each with diameter nine, the leaves that form the ends
# of a longest path are shaded (note that there is more than one path in each tree of length nine, but
# no path longer than nine nodes).

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def get_leaves_distance(self, leaf1, leaf2):
        i = 0
        while leaf1[i]==leaf2[i]:
            i +=1
        return len(leaf1) + len(leaf2) - i


    def find_leaves(self, tree):
        if not tree:
            return []
        if not tree.left and not tree.right:
            return [tree]
        left_leaves = [[tree] + leaf for leaf in self.find_leaves(tree.left)]
        right_leaves = [[tree] + leaf for leaf in self.find_leaves(tree.right)]
        return left_leaves + right_leaves


    def find_diameter(self, tree):
        leaves = self.find_leaves(tree)
        longest = max( [len(leaf) for leaf in leaves] )

        for i in range(len(leaves)-1):
            for j in range(i+1, len(leaves)):
                distance = self.get_leaves_distance(leaves[i], leaves[j])
                if distance > longest:
                    longest = distance
        return  longest


