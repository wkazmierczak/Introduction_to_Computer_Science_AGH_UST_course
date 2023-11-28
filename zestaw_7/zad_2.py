# 2. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.


class Node:
    def __init__(self, idx, value, next=None):
        self.idx = idx
        self.value = value
        self.next = next


def value_at_given_index(g, idx):
    curr = g
    while curr is not None:
        if curr.idx == idx and curr.idx >= 0:
            return curr.value
        curr = curr.next


def substitute(g, idx, new_val):
    curr = g
    while curr is not None:
        if curr.idx == idx:
            curr.value = new_val
            return
        if curr.next.idx > idx:
            q = Node(idx, new_val, curr.next)
            curr.next = q
            return
        curr = curr.next


def print_all(g):
    curr = g
    while curr is not None:
        print(f"Index {curr.idx}: {curr.value}")
        curr = curr.next


if __name__ == '__main__':
    g = Node(-1, -1)

    a = Node(0, 23)
    b = Node(3, 25)
    c = Node(7, 43)

    a.next = b
    b.next = c
    g.next = a

    #print(value_at_given_index(g, -1))
    substitute(g, 5, 12)
    substitute(g, 7, 22)

    print_all(g.next)