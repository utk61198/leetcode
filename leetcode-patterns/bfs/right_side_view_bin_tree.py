# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            ans=[]
            q=[root]
            while len(q)!=0:
                end=len(q)
                for i in range(end):
                    temp=q.pop(0)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                    if i == end-1:
                        ans.append(temp.val)
            return ans