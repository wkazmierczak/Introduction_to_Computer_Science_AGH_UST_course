# 3. Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
# funkcję, która usuwa z listy wejściowej najkrótszą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
# dokładnie jednej najkrótszej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
# Funkcja powinna zwrócić liczbę usuniętych elementów.
# Na przykład z listy [ 1 3 3 3 3 5 7 11 13 13 13 1 2 2 2 2 3 ] należy usunąć podlistę [13 13 13],
# a z listy [1 3 3 3 3 5 7 11 13 13 13 1 2 2 2 3 ] nie należy nic usuwać.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def func(head):
    w = head
    p = head
    q = p.next
    min_1 = float('inf')
    while p is not None:
        cnt = 1
        while q is not None and p.value == q.value:
            cnt += 1
            q = q.next
        if cnt > 1:
            min_1 = min(cnt, min_1)
            w.next = q
        p.next = q
        p = p.next
        if q is not None:
            q = q.next
    return min_1


def printall(p):
    while p is not None:
        print(p.value)
        p = p.next


if __name__ == '__main__':
    first = Node(4)
    second = Node(10)
    third = Node(10)
    fourth = Node(3)
    fifth = Node(10)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    g = Node(None, first)

    print(func(first))
    print("___________")
    printall(first)
