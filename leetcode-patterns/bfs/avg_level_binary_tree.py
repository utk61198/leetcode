# https://leetcode.com/problems/average-of-levels-in-binary-tree/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root==None:
            return []
        else:
            q=[]
            ans=[]
            q.append(root)
            while len(q)!=0:
                level_sum=0
                total=len(q)
                for i in range(len(q)):
                    temp=q.pop(0)
                    level_sum+=temp.val
                    if temp.left!=None:
                        q.append(temp.left)
                    if temp.right!=None:
                        q.append(temp.right)
                ans.append(float(level_sum/total))
            return ans