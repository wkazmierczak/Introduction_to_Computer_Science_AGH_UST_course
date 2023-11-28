# 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def usuwanie_co_drugiego(g):
    p = g
    while p.next is not None:
        if p.next.next is None:
            p.next = None
            return
        p.next = p.next.next
        p = p.next


def print_all(g):
    p = g
    while p is not None:
        if p.value is not None:
            print(p.value)
        p = p.next


if __name__ == '__main__':
    first = Node(2)
    second = Node(4)
    third = Node(6)
    fourth = Node(8)
    fifth = Node(10)
    sixth = Node(12)
    seventh = Node(14)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    g = Node(None, first)

    print_all(first)
    print("___________________________________")
    usuwanie_co_drugiego(first)
    print_all(first)
