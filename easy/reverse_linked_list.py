

from typing import Optional


class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]):
    current = head
    previous = None

    while current is not None:
        reference = current.next
        current.next = previous
        previous = current
        current = reference

    return previous


