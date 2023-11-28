# 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
# zwraca wskaźnik do ostatniego elementu przed cyklem.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def zad_25(g):
    p = g.next
    objects = []
    while p is not g:
        if p in objects:
            idx = objects.index(p)
            return objects[idx-1].value
        objects.append(p)
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
    fifth.next = fourth

    g = Node(None, first)

    print(zad_25(g.next))