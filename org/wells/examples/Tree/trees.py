class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children


def search_deepest_path(root: Node):
    max_path = []
    max_length = 0
    for child in root.children:
        p = search_deepest_path(child)
        p_length = len(p)
        if p_length > max_length:
            max_length = p_length
            max_path = p
    if max_length == 0:
        return [root]
    max_path.insert(0, root)
    return max_path


def tree_compute(node, context, node_fn, aggregate_fn):
    node_context = node_fn(context, node)
    aggregate_context = node_context
    for child in node.children:
        aggregate_context = aggregate_fn(aggregate_context, tree_compute(child, node_context, node_fn, aggregate_fn))
    print("result for %s : %s" % (node.data, aggregate_context))
    return aggregate_context

# Given a tree with each node having numbers. Path from root to a leaf node forms a number like
# (root(1)->left(2)->leftLeaf(3) = 123). He asked me to code to add all the number for root to leaf.


def leaf_add(root):
    def node_fn(context, node):
        result, parent = context
        if len(node.children) == 0:
            result = parent * 10 + node.data
            return result, parent
        else:
            return result, parent * 10 + node.data

    def aggregate_fn(aggregate_context, context):
        aggregate_result, aggregate_parent = aggregate_context
        result, parent = context
        return aggregate_result + result, aggregate_parent

    result, _ = tree_compute(root, (0, 0), node_fn, aggregate_fn)
    return result


def tree_add(root):
    def node_fn(context, node):
        _, parent = context
        return parent * 10 + node.data, parent * 10 + node.data

    def aggregate_fn(aggregate_context, context):
        aggregate_result, aggregate_parent = aggregate_context
        result, parent = context
        return aggregate_result + result, aggregate_parent

    result, _ = tree_compute(root, (0, 0), node_fn, aggregate_fn)
    return result


def build_tree():
    return Node(1, [Node(2, [Node(3, [Node(4, []),
                                      Node(5, [])])]),
                    Node(6, [Node(7, [Node(8, []),
                                      Node(9, [Node(9, [])])])])])


def tree_test():
    root = build_tree()
    print(leaf_add(root))
    print(tree_add(root))


tree_test()


def print_path(path):
    print([node.data for node in path])


def test_search():
    root = build_tree()
    print_path(search_deepest_path(root))


# test_search()
a = [1, 2]
a.pop(1)


