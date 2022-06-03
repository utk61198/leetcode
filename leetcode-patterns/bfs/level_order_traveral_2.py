# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        else:
            ans=[]
            q=[root]
            while len(q)!=0:
                ans_temp=[]
                for i in range(len(q)):
                    temp=q.pop(0)
                    ans_temp.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                ans.append(ans_temp)
            return ans[::-1]