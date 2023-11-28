# 23. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def cycle_length(head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            cnt = 0
            while slow.next != fast.next.next:
                cnt += 1
                fast = fast.next.next
                slow = slow.next
            return cnt + 1
    return False


if __name__ == '__main__':
    first = Node(2)
    second = Node(4)
    third = Node(6)
    fourth = Node(8)
    fifth = Node(10)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    print(cycle_length(first))