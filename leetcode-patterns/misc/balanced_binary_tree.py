# https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l = self.height(root.left)
        r = self.height(root.right)
        if abs(l-r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
        