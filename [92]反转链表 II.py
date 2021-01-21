# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return head
        pre = None
        cur = head
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        tail, con = cur, pre
        while n:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            n -= 1
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head
