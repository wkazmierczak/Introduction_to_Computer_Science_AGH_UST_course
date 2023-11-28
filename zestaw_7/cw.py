class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


z = Node(3)
y = Node(2, z)
x = Node(1, y)

a = x
while a is not None:
    print(a.value)
    a = a.next
