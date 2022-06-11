# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        else:
            ans=[]
            q=[]
            q.append(root)
            while len(q)!=0:
                temp=[]
                for i in range(len(q)):
                    temp_node=q.pop(0)
                    temp.append(temp_node.val)
                    if temp_node.left:
                        q.append(temp_node.left)
                    if temp_node.right:
                        q.append(temp_node.right)
                ans.append(temp)
            return ans
        