# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, a: ListNode, b: ListNode) -> ListNode:
        pre = None
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        a = b = head
        for i in range(k):
            if b is None:
                return head
            b = b.next
        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
