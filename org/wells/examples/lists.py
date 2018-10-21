class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedItem:
    def __init__(self, data):
        self.data = data
        self.next_list = None
        self.next = None


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, node: LinkedNode):
        if self.head is None:
            self.head = node
        elif node.data < self.head.data:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current is not None:
                if current.next is None:
                    current.next = node
                    return
                elif node.data < current.next.data:
                    node.next = current.next
                    current.next = node
                    return
                else:
                    current = current.next

    def pop(self):
        result = self.head
        self.head = self.head.next
        return result

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


def test_ordered_list():
    l = OrderedList()
    for i in [3, 5, 2, 4, 6, 8]:
        l.add(LinkedNode(i))
    l.print()
    l.pop()
    print('----')
    l.print()

test_ordered_list()

# A group of people are seated in a circular table. After a while , each members takes a chit and writes his name along
# with the next person name (anticlock wise.)   . If such chits are given , re draw the the table. A optimal approach was
# expected. eg. A – B – C- D – E – A
# chits will be written as A-B
# B-C
# C-D etc
# Same questions as above . if each member takes a chit and writes his neighbors name . re draw the table.

def rebuild_neighbors_2(chits):
