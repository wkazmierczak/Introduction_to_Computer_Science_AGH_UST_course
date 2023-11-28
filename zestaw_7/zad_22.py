# 22. Dana jestlista, który być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
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
    fourth.next = third

    print(has_cycle(first))