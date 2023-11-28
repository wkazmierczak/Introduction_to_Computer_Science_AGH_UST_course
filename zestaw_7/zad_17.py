# 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        # self.prev = prev
        self.next = next


def odd_number_of_ones_in_binary(num):
    cnt = 0
    while num > 0:
        x = num % 2
        if x == 1:
            cnt += 1
        num //= 2
    return cnt % 2 == 1


def zad_17(p):
    while p is not None:
        if odd_number_of_ones_in_binary(p.value):
            if p.next is None:
                p.prev.next = p.next
            else:
                p.prev.next = p.next
                p.next.prev = p.prev
        p = p.next


def usun_elem(head):
    p = head
    i = head
    while i.next is not None:
        i = i.next
        if not odd_number_of_ones_in_binary(i.value):
            p.next = i
            p = p.next
    p.next = None


def print_all(p):
    while p is not None:
        print(p.value)
        p = p.next


if __name__ == '__main__':
    x = Node(1)
    y = Node(61)
    z = Node(12)
    a = Node(15)
    b = Node(11)
    c = Node(3)

    # g = Node(None, None, x)
    #
    # x.next, x.prev = y, g
    # y.next, y.prev = z, x
    # z.next, z.prev = a, y
    # a.next, a.prev = b, z
    # b.next, b.prev = c, a
    # c.next, c.prev = None, b
    #
    # zad_17(g.next)
    # print_all(g.next)

    x.next = y
    y.next = z
    z.next = a
    a.next = b
    b.next = c

    g = Node(None, x)

    print_all(g)
    usun_elem(g)
    print("_________________")
    print_all(g)
