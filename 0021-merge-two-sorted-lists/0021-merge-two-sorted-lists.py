# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        i,j = 0, 0
        merged_list = ListNode(-1, None)
        final = merged_list
        
        while list1 or list2:
            if (list1 and (not list2 or list1.val <= list2.val)):
                nodeToTake = list1
                list1 = list1.next
            else:
                nodeToTake = list2
                list2 = list2.next

            merged_list.next = ListNode(nodeToTake.val)
            merged_list = merged_list.next
            
        return final.next
        
        
        
        
        