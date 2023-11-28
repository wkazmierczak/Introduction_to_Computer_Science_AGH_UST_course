# 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy.
from zad_8 import print_all


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def zad_11(p, value):
    while p.next is not None:
        if p.next.value == value:
            p.next = p.next.next
            return
        p = p.next
    q = Node(value)
    p.next = q


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

    print_all(g)
    zad_11(g, 3)
    print("__________________")
    print_all(g)

