# 24. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów przed cyklem.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def before_cycle_length(head):
    fast = head
    slow = head
    cnt = 0
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            n = head
            while n != slow:
                cnt += 1
                n = n.next
                slow = slow.next
            return cnt
    w = head
    while w is not None:
        cnt += 1
        w = w.next
    return cnt


if __name__ == '__main__':
    first = Node(2)
    second = Node(4)
    third = Node(6)
    fourth = Node(8)
    fifth = Node(10)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = third

    print(befor_cycle_length(first))