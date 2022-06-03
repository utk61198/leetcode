# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        else:
            direction = -1
            q = [root]
            ans = []
            while len(q) != 0:
                ans_temp = []
                for i in range(len(q)):
                    temp = q.pop(0)
                    ans_temp.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                if direction == 1:
                    ans.append(ans_temp[::-1])
                    direction = -1
                else:
                    ans.append(ans_temp)
                    direction = 1
            return ans
