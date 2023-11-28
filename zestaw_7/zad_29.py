# 29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
# naturalne. W obu listach liczby są posortowane rosnąco. Proszę napisać
# funkcję usuwającą z każdej listy liczby nie występujące w drugiej. Do
# funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
# łączną liczbę usuniętych elementów.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def usuwanie_elem(head_1, head_2):
    p = head_1
    q = head_2
    cnt = 0
    while p.next is not None and q.next is not None:
        if p.next.value > q.next.value:
            q.next = q.next.next
            cnt += 1
        elif p.next.value < q.next.value:
            p.next = p.next.next
            cnt += 1
        else:
            p = p.next
            q = q.next
    p.next = None
    q.next = None
    return cnt


def printall(w):
    while w is not None:
        if w.value is not None:
            print(w.value)
        w = w.next


if __name__ == '__main__':
    first = Node(2)
    second = Node(4)
    third = Node(6)
    fourth = Node(8)
    fifth = Node(10)

    x = Node(3)
    y = Node(6)
    z = Node(7)
    a = Node(10)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    x.next = y
    y.next = z
    z.next = a

    g1 = Node(None, first)
    g2 = Node(None, x)

    print(usuwanie_elem(g1, g2))

    printall(g2)

