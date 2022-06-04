# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        else:
            q = [root]
            while len(q) != 0:
                l = len(q)
                for i in range(l):
                    temp = q.pop(0)
                    if i == l-1:
                        temp.next = None
                    else:
                        temp.next = q[0]
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
            return root


# solution using only one loop
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        else:
            q = [root]
            qn = []
            while len(q):
                temp = q.pop(0)
                if temp.left:
                    qn.append(temp.left)
                if temp.right:
                    qn.append(temp.right)
                if q:
                    temp.next = q[0]
                else:
                    q = qn
                    qn = []
            return root
