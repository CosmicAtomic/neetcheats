# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        prev = 0
        dummy = ListNode()
        curRes = dummy
        while cur1 or cur2 or prev!= 0:
            a = cur1.val if cur1 else 0
            b = cur2.val if cur2 else 0
            curRes.next = ListNode(val=(prev + a + b)%10)
            prev = (prev + a + b)//10
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            curRes = curRes.next
        return dummy.next




        