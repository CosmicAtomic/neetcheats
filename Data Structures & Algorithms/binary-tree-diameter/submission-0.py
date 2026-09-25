# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def go_search(curr):
            nonlocal res
            if not curr: return 0
            left = go_search(curr.left)
            right = go_search(curr.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        go_search(root)
        return res


        