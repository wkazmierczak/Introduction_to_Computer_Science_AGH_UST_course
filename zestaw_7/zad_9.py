# 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
# elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
# zwiększającą taką liczbę o 1.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_one(g):
    p = g
    while p.next.next is not None:
        p = p.next
    if p.next.value + 1 < 10:
        p.next.value += 1
    else:
        if p.value is None:
            p.value = 0
        p.value += 1
        p.next.value = (p.next.value + 1)%10


def print_all(g):
    p = g
    while p is not None:
        if p.value is not None:
            print(p.value, end="")
        p = p.next
    print("")
    print("--------------------------------")


if __name__ == '__main__':
    first = Node(9)
    # second = Node(8)
    # third = Node(6)
    # fourth = Node(8)

    # first.next = second
    # second.next = third
    # third.next = fourth

    g = Node(None, first)

    print_all(g)
    add_one(g)
    print_all(g)
    add_one(g)
    print_all(g)
    add_one(g)
    print_all(g)