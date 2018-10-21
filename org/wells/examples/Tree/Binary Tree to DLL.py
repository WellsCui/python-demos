class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class DllNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def link_next(self, node):
        if node is not None:
            self.next = node
            node.previous = self

    @staticmethod
    def tail(node):
        if node is None:
            return None
        while node.next is not None:
            node = node.next
        return node


class BinaryTreeToDll:
    @staticmethod
    def getOrderedList(bt_node):
        if bt_node is None:
            return []
        return BinaryTreeToDll.getOrderedList(bt_node.left) + \
               [DllNode(bt_node.data)] + BinaryTreeToDll.getOrderedList(bt_node.right)

    @staticmethod
    def ls_to_dll(lst):
        if len(lst) == 0:
            return None
        head = None
        prev = None
        for next_node in lst:
            if head is None:
                head = next_node
            if prev:
                prev.link_next(next_node)
            prev = next_node
        return head

    @staticmethod
    def transfer(bt_node):
        ls = BinaryTreeToDll.getOrderedList(bt_node)
        return BinaryTreeToDll.ls_to_dll(ls)

    @staticmethod
    def transfer2(bt_node):
        if bt_node is None:
            return []
        rs = BinaryTreeToDll.transfer2(bt_node.left)
        if len(rs) == 0:
            rs = [DllNode(bt_node.data)]
        else:
            dll_node = DllNode(bt_node.data)
            rs[-1].link_next(dll_node)
            rs = rs + [dll_node]
        right_lst = BinaryTreeToDll.transfer2(bt_node.right)
        if len(right_lst) > 0:
            rs[-1].link_next(right_lst[0])
            rs = rs + right_lst
        return rs





def build_tree():
    root = BTNode(25)
    root.left = BTNode(11)
    root.right = BTNode(43)
    root.left.left = BTNode(5)
    root.left.right = BTNode(17)
    root.left.left.left = BTNode(3)
    root.left.left.right = BTNode(6)
    root.left.right.left = BTNode(13)
    root.left.right.right = BTNode(23)
    root.right.left = BTNode(33)
    root.right.left.left = BTNode(29)
    root.right.left.right = BTNode(42)
    root.right.right = BTNode(51)
    root.right.right.left = BTNode(44)
    root.right.right.right = BTNode(53)
    return root


def test_transfer():
    dll = BinaryTreeToDll.transfer2(build_tree())[0]
    while dll:
        print(str(dll.data))
        dll = dll.next

test_transfer()


