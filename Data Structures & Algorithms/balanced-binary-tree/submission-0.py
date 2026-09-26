# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height(self, root):
        if not root: return 0
        res = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return res
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftHeight = self.get_height(root.left)
        rightHeight = self.get_height(root.right)
        notBalanced =  abs(leftHeight-rightHeight) > 1
        return (not notBalanced) and self.isBalanced(root.left) and self.isBalanced(root.right)

        

        