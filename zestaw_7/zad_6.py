# 6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_elem(q, value):
    p = q
    while p.next is not None:
        p = p.next
    t = Node(value)
    p.next = t


def print_all(g):
    while g is not None:
        print(g.value)
        g = g.next


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

    add_elem(g.next, 12)
    print_all(g.next)