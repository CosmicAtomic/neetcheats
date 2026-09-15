"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        copied_head = Node(
                x = head.val
            )
        copied_curr = copied_head
        nodeMap = {head: copied_head}
        curr = head.next
        while curr:
            new_node = Node(
                x = curr.val
            )
            copied_curr.next = new_node
            copied_curr = copied_curr.next
            nodeMap[curr] = copied_curr
            curr = curr.next
        curr = head
        copied_curr = copied_head
        while curr:
            if curr.random:
                copied_curr.random = nodeMap[curr.random]
            else:
                copied_curr.random = None
            curr = curr.next
            copied_curr = copied_curr.next
        return copied_head

        



            

        