# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
            
        ptr = head
        
        while list1 is not None or list2 is not None:
            if list2 is None or (list1 is not None and list1.val < list2.val):
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
            
            
        return head