from abc import ABCMeta, abstractmethod


class BinaryTreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class RetrospectableBinaryTreeNode(BinaryTreeNode):
    def __init__(self, ancestor, data, left, right):
        super().__init__(data, left, right)
        self.ancestor = ancestor


class RetrospectableBinaryTreeNodeExplorer:
    def __init__(self, context, visit_fn, terminated):
        self.context = context
        self.visit_fn = visit_fn
        self.terminated = terminated

    def explore_ancestor(self, node: RetrospectableBinaryTreeNode, path):
        self.context = self.visit_fn(node.ancestor, self.context, path)
        path += [node]
        if self.terminated(self.context):
            self.context['path'] = path
            return
        if node.ancestor.left == node:
            self.explore_as_root(node.ancestor.right, path)
        else:
            self.explore_as_root(node.ancestor.left, path)
        if self.terminated(self.context):
            return
        self.explore_ancestor(node.ancestor, path)

    def explore_as_root(self, node: RetrospectableBinaryTreeNode, path):
        self.context = self.visit_fn(node, self.context, path)
        path += [node]
        if self.terminated(self.context):
            self.context['path'] = path
            return
        for child in [node.left, node.right]:
            self.explore_as_root(child, path)
            if self.terminated(self.context):
                return

    def explore(self, node: RetrospectableBinaryTreeNode):
        self.explore_as_root(node, [])
        if self.terminated(self.context):
            return self.context
        self.explore_ancestor(node, [node])
        return self.context


def bt2rbt(root: BinaryTreeNode, ancestor: RetrospectableBinaryTreeNode):
    new_root = RetrospectableBinaryTreeNode(ancestor, root.data, None, None)
    new_root.left = bt2rbt(root.left, new_root)
    new_root.right = bt2rbt(root.right, new_root)
    return new_root


#
# Find the distance between two keys in a binary tree, no parent pointers are given.
# Distance between two nodes is the minimum number of edges to be traversed to reach one node from other.
#
# Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)
# 'n1' and 'n2' are the two given keys
# 'root' is root of given Binary Tree.
# 'lca' is lowest common ancestor of n1 and n2
# Dist(n1, n2) is the distance between n1 and n2.

def get_ancestors_from_root(root, nodes):
    result = {}

    border = [(root, [])]

    def breadth_first_explore():
        while len(border) > 0 and len(nodes) > 0:
            current, path = border.pop(0)
            if current in nodes:
                result[current] = path
                nodes.remove(current)

            new_path = path + [current]
            if current.left is not None:
                border.append((current.left, new_path))
            if current.right is not None:
                border.append((current.right, new_path))

    breadth_first_explore()
    return result


def test_get_ancestors_from_root():
    root = BinaryTreeNode(0, None, None)
    nd1 = BinaryTreeNode(1, None, None)
    nd2 = BinaryTreeNode(2, None, None)
    nd3 = BinaryTreeNode(3, None, None)
    nd4 = BinaryTreeNode(4, None, None)
    nd5 = BinaryTreeNode(5, None, None)
    nd6 = BinaryTreeNode(6, None, None)
    nd7 = BinaryTreeNode(7, None, None)
    nd8 = BinaryTreeNode(8, None, None)
    nd9 = BinaryTreeNode(9, None, None)
    root.left = nd1
    root.right = nd2
    nd1.left = nd3
    nd1.right = nd4
    nd2.left = nd5
    nd2.right = nd6
    nd3.left = nd7
    nd3.right = nd8
    nd4.right = nd9
    result = get_ancestors_from_root(root, [nd7, nd8, nd9])

    def print_node_path(nd, path):
        print("node: %s ancestors: %s" % (nd.data, [n.data for n in path]))

    for nd in result:
        print_node_path(nd, result[nd])


# test_get_ancestors_from_root()


# A binary search tree (BST) is a node based binary tree data structure which has the following properties.
# • The left subtree of a node contains only nodes with keys less than the node’s key.
# • The right subtree of a node contains only nodes with keys greater than the node’s key.
# • Both the left and right subtrees must also be binary search trees.
#
# From the above properties it naturally follows that:
# • Each node (item in the tree) has a distinct key.

def validate_bst(root: BinaryTreeNode):
    if root is None:
        return True, None, None

    left_valid, left_min, left_max = validate_bst(root.left)
    right_valid, right_min, right_max = validate_bst(root.right)

    valid = left_valid and right_valid and \
            (right_min is None or right_min > root.data) and \
            (left_max is None or left_max < root.data)

    tree_min = root.data if left_min is None or left_min > root.data else left_min
    tree_min = tree_min if right_min is None or right_min > tree_min else right_min
    tree_max = root.data if right_max is None or right_max < root.data else right_max
    tree_max = tree_max if left_max is None or left_max < tree_max else left_max

    return valid, tree_min, tree_max


def validate_bst_test():
    root = BinaryTreeNode(0, None, None)
    nd1 = BinaryTreeNode(1, None, None)
    nd2 = BinaryTreeNode(2, None, None)
    nd3 = BinaryTreeNode(3, None, None)
    nd4 = BinaryTreeNode(4, None, None)
    nd5 = BinaryTreeNode(5, None, None)
    nd6 = BinaryTreeNode(6, None, None)
    nd7 = BinaryTreeNode(7, None, None)
    nd8 = BinaryTreeNode(8, None, None)
    nd9 = BinaryTreeNode(9, None, None)
    root.left = nd1
    root.right = nd2
    nd1.left = nd3
    nd1.right = nd4
    nd2.left = nd5
    nd2.right = nd6
    nd3.left = nd7
    nd3.right = nd8
    nd4.right = nd9
    print(validate_bst(root))

    root.data = 6
    nd1.data = 3
    nd2.data = 8
    nd3.data = 1
    nd4.data = 4
    nd5.data = 7
    nd6.data = 9
    nd7.data = 0
    nd8.data = 2
    nd9.data = 5
    print(validate_bst(root))


# validate_bst_test()


# Given a Binary Search Tree (BST), modify it so that all greater values in the given BST are added to every node.
# For example, consider the following BST.

#            50
#         /      \
#      30        70
#     /   \      / \
#     20    40 60   80
#
# The above tree should be modified to following
#
#           260
#         /       \
#     330        150
#     /   \       / \
#     350   300 210   80


class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def binary_tree_right_first_walk(node: BinaryNode, context, visit_fn):
    if node is None:
        return context
    context = binary_tree_right_first_walk(node.right, context, visit_fn)
    context = visit_fn(node, context)
    return binary_tree_right_first_walk(node.left, context, visit_fn)


def binary_tree_add_greater_values(node: BinaryNode):
    def visit_fn(nd, context):
        nd.data += context
        return nd.data

    return binary_tree_right_first_walk(node, 0, visit_fn)


def get_tree_height(node: BinaryNode):
    if node is None:
        return 0
    else:
        return 1 + max(get_tree_height(node.left), get_tree_height(node.right))


def binary_tree_add_greater_values_test():
    binary_tree_data = [50, 30, 70, 20, 40, 60, 80]
    nodes = [BinaryNode(data) for data in binary_tree_data]
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    binary_tree_add_greater_values(root)
    for nd in nodes:
        print(nd.data)


# binary_tree_add_greater_values_test()


# Given a Binary tree with  root(R) , a node(N) and distance (k). find all the nodes at k distance from N. Optimal solution was expected.

def find_path_from_root(root: BinaryNode, node: BinaryNode):
    if root is None:
        return None
    elif root == node:
        return [root]
    else:
        sub_path = find_path_from_root(root.right, node)
        if sub_path:
            return [root] + sub_path
        sub_path = find_path_from_root(root.left, node)
        if sub_path:
            return [root] + sub_path
        return None


def find_all_k_distance_from_root(root, k):
    if root is None:
        return []
    if k == 0:
        return [root]
    return find_all_k_distance_from_root(root.right, k-1) + find_all_k_distance_from_root(root.left, k-1)


def find_all_k_distance(root, node, k):
    path = find_path_from_root(root, node)
    if path is None:
        return []
    for n in path:
        print(n.data)
    path.reverse()
    deep = len(path)
    rs = []

    for d in range(deep):
        if d == k:
            rs.append(path[d])
            break
        if d == 0:
            rs = rs + find_all_k_distance_from_root(path[d], k)
        else:
            r = path[d].left if path[d].right == path[d-1] else path[d].right
            rs = rs + find_all_k_distance_from_root(r, k-d)
    return rs

def find_all_k_distance_test(node_count, node_index, distance):
    root = BinaryNode(-1)
    node = None
    leaves = [root]
    for i in range(node_count):
        p = leaves.pop(0)
        if i == node_index:
            node = p
        p.left = BinaryNode(2*i)
        p.right = BinaryNode(2*i+1)
        leaves = leaves + [p.left, p.right]

    nodes = find_all_k_distance(root, node, distance)
    print('all node %d distance to node %d' % (distance, node.data))
    for n in nodes:
        print(n.data)


find_all_k_distance_test(20, 5, 2)






