# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                temp = ptr.next.next if ptr.next.next else None
                ptr.next = temp
            else:
                ptr = ptr.next
        return head



        



