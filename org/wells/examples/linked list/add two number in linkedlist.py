# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        header = None
        current = None

        def appendNode(node):
            nonlocal header
            nonlocal current

            if header is None:
                header = node
                current = node
            else:
                current.next = node
                current = node

        sign = 0
        while l1 or l2:
            if l1 is None:
                val = l2.val + sign
                l2 = l2.next

            elif l2 is None:
                val = l1.val + sign
                l1 = l1.next

            else:
                val = l1.val + l2.val + sign
                l1 = l1.next
                l2 = l2.next

            if val > 9:
                sign = 1
                appendNode(ListNode(val - 10))
            else:
                sign = 0
                appendNode(ListNode(val))

        if sign == 1:
            appendNode(ListNode(sign))
        return header


n1 = ListNode(5)
n1.next = ListNode(7)
n1.next.next = ListNode(7)
n2 = ListNode(8)
n2.next = ListNode(6)
n2.next.next = ListNode(3)

rs = Solution().addTwoNumbers(n1, n2)

while rs is not None:
    print(rs.val)
    rs = rs.next


