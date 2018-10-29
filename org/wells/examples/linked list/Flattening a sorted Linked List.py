# Given a Linked List where every node represents a linked list and contains two pointers of its type:
# (i) a next pointer to the next node
# (ii) a bottom pointer to a linked list where this node is head.
#
# You have to flatten the linked list to a single linked list which is sorted.


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(LinkedNode):
    def __init__(self, data):
        super().__init__(data)
        self.next_list = None


class SortedLinkedListFlattener:

    def merge_list(self, list1, list2):
        head = None
        while list1 or list2:
            if not list1:
                next_node = list2
                list2 = list2.next
            elif not list2:
                next_node = list1
                list1 = list1.next
            elif list1.data < list2.data:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next
            if head:
                head.next = LinkedNode(next_node.data)
                head = head.next
            else:
                head = LinkedNode(next_node.data)
        return head

    def flatten(self, linked_node: LinkedList):
        result = None
        while linked_node:
            if result:
                result = self.merge_list(result, linked_node)
            else:
                result = linked_node
            linked_node = linked_node.next_list



