# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def if_contains(g, elem):
    if g is None:
        return False
    if g.value == elem:
        return True
    elif g.next.value > elem:
        return False
    return if_contains(g.next, elem)


def add(g, new_val):
    if g.next is None:
        q = Node(new_val)
        q.next = g.next
        g.next = q
        return
    if g.next is not None:
        if g == new_val:
            return
        elif g.next.value > new_val:
            q = Node(new_val)
            q.next = g.next
            g.next = q

            return
        add(g.next, new_val)


def delete(p, elem):
    if p.next.value == elem:
        p.next = p.next.next
        return
    if p.next is None:
        return
    if p.next.value > elem:
        return
    delete(p.next, elem)


def print_all(g):
    while g is not None:
        print(g.value)
        g = g.next


if __name__ == '__main__':
    z = Node(3)
    y = Node(2, z)
    x = Node(1, y)

    g = Node(0, x)

    add(g, 34)
    add(g, 5)
    add(g, 27)

    delete(g, 5)
    delete(g, 3)

    add(g, 5)

    print_all(g.next)

    print(if_contains(g, 3))

