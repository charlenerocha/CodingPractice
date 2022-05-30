# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start, end = head, head
        even = False
        
        while end.next != None:
            end = end.next
            
            if even:
                even = False
            else:
                start = start.next
                even = True
            
        return start