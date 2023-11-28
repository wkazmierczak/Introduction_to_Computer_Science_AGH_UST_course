# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.

class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


def reverse_elements(g):
    r = g.next
    while r is not None:
        print(r.value)
        a = r.next
        b = a.next
        r = a.next
        a = b


if __name__ == '__main__':
    first = Node(2)
    second = Node(4)
    third = Node(6)
    fourth = Node(8)
    fifth = Node(10)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    g = Node(None, first)

    reverse_elements(g)