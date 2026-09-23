# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for node_list in lists:
            while node_list:
                nodes.append(node_list.val)
                node_list = node_list.next
        nodes.sort()

        dummy = ListNode()
        curr = dummy
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        return dummy.next
        
        