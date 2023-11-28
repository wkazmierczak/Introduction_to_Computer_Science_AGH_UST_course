# 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
# powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
# wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def check_if_positive_even(num):
    return num > 0 and num % 2 == 0


def check_if_negative_odd(num):
    return num < 0 and num % 2 == 1


def func(d_head, w_head_1, w_head_2):
    cnt = 0
    while d_head.next is not None:
        d_head = d_head.next
        if check_if_positive_even(d_head.value):
            w_head_1.next = d_head
            w_head_1 = w_head_1.next
        elif check_if_negative_odd(d_head.value):
            w_head_2.next = d_head
            w_head_2 = w_head_2.next
        else:
            cnt += 1
    w_head_1.next = None
    w_head_2.next = None
    return cnt


def print_all(p):
    while p is not None:
        print(p.value)
        p = p.next


if __name__ == '__main__':
    first = Node(5)
    second = Node(-1)
    third = Node(6)
    fourth = Node(-77)
    fifth = Node(-6)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    g = Node(None, first)
    w1 = Node(None)
    w2 = Node(None)

    print(func(g, w1, w2))
    print("___________")
    print_all(w1)
    print("__________")
    print_all(w2)

