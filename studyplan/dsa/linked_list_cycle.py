#https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        else:
            slow=head
            fast=head
            ans=False
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    ans=True
                    break
            return ans