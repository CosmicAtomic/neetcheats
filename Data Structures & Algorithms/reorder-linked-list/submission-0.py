# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeArr = []
        node = head
        while node:
            nodeArr.append(node)
            node = node.next
        l = 0
        r = len(nodeArr) - 1
        while l< r:
            nodeArr[l].next = nodeArr[r]
            l += 1
            if l >= r:
                break
            nodeArr[r].next = nodeArr[l]
            r -= 1
        nodeArr[l].next = None
        


