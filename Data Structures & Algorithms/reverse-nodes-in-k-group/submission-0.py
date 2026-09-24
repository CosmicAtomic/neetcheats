# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_linked_list(self, head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        Kcount = 1
        cur = head
        while cur and Kcount < k:
            cur = cur.next
            Kcount += 1
        if not cur:
            return head
        next_list = cur.next
        cur.next = None
        l_reverse = self.reverse_linked_list(head)
        head.next = self.reverseKGroup(next_list, k)
        return l_reverse





        