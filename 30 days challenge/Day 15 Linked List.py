class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        for x in elems:
            print(x, end=' ')


mylist = Solution()
T = int(input())
for i in range(T):
    data = int(input())
    mylist.insert(data)
mylist.display()
