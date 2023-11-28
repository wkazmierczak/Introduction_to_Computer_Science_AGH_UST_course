# 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def deleting_last_elem(g):
    p = g
    while p.next.next is not None:
        p = p.next
    p.next = None


def print_all(g):
    p = g
    while p is not None:
        print(p.value)
        p = p.next


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

    deleting_last_elem(first)
    deleting_last_elem(first)
    print_all(first)