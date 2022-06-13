# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q=[]
        q.append(root)
        level=1
        while len(q)!=0:
            for i in range(len(q)):
                temp=q.pop(0)
                if temp.right == None and temp.left ==None:
                    return level
                else:
                    if temp.left!=None:
                        q.append(temp.left)
                    if temp.right!=None:
                        q.append(temp.right)
            level+=1
        return -1
        