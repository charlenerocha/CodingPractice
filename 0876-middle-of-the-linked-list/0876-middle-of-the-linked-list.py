# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
         # Returning head if length < 2
        if head is None or head.next is None:    
            return head

        mid, end = head, head.next

        # Continue while we have not reached the end of the linked list
        while end is not None and end.next is not None and end.next.next is not None:
            mid = mid.next
            end = end.next.next

        return mid.next