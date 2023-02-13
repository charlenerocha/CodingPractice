# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # tortoise and hare algorithm
        
        tort = head
        if head:    hare = head.next
        
        while tort and hare:
            if tort == hare:
                return True
            
            tort, hare = tort.next, hare.next
            if hare:    hare = hare.next
            
        return False