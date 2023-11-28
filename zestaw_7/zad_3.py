# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge(p, q):
    while p is not None and q is not None:
        if p.value >= q.value:
            q.next, q = p, q.next
        elif p.value < q.value:
            p.next, p = q, p.next


def merge_rec(p, q):
    if p is None:
        return q
    if q is None:
        return p
    if p.value <= q.value:
        p.next = merge_rec(p.next, q)
        return p
    else:
        q.next = merge_rec(p, q.next)
        return q


def print_all(p, q):
    if p.value > q.value:
        g = q
    else:
        g = p
    while g is not None:
        print(g.value)
        g = g.next


if __name__ == '__main__':
    z = Node(9)
    y = Node(5, z)
    x = Node(3, y)

    c = Node(9)
    b = Node(5, c)
    a = Node(4, b)

    p = Node(0, x)
    q = Node(0, a)

    merge_rec(p.next, q.next)

    print_all(p.next, q.next)

