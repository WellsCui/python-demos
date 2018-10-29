# Add two integers represented by singly linked lists to produce the resultant linked list which represents the sum as follows :
# Linked List 1 : 1->2->3 (Number : 123)
# Linked List 2 : 1->2->3 (Number : 123)
# Resultant Linked List : 2->4->6 (Number : 246)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def add_two_num(self, num1, num2):
        rs = num1 + num2
        if rs > 9:
            return rs-10, 1
        else:
            return rs, 0

    def add_linked_list(self, lst1, lst2):
        if not lst1 and not lst2:
            return None, 0
        elif not lst1.next and not lst2.next:
            rs, flag = self.add_two_num(lst1.data, lst2.data)
            return Node(rs), flag
        elif lst1.next and lst2.next:
            rs, flag = self.add_two_num(lst1.data, lst2.data)

        elif not lst1.next:
            rs, flag = self.add_linked_list(lst1, lst2.next)
            return Node(rs), flag


            return lst2, 0
        elif not lst2.next:
            return lst1, 0
        else:

