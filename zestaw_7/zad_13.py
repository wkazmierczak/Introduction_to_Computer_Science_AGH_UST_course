# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def zad_13(head):
    i = head.next
    p = head.next
    while i.next is not None:
        if i.next.value > i.value:
            p.next = i.next
            p = p.next
        i = i.next
    p.next = None


def rek(head):
    if head.next is None:
        return
    rek(head.next)
    if head.next.value < head.value:
        head.next = head.next.next


def print_all(p):
    while p is not None:
        print(p.value)
        p = p.next


if __name__ == '__main__':
    first = Node(5)
    second = Node(3)
    third = Node(7)
    fourth = Node(2)
    fifth = Node(8)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    g = Node(None, first)

    print_all(g.next)
    print("___________________")
    rek(g.next)
    print_all(g.next)