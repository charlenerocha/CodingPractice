# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = added = ListNode(0)
        
        carryOver = 0
        
        while l1 or l2:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            
            sum = carryOver + x + y
            carryOver = sum / 10
            
            added.next = ListNode(sum % 10)
                
            added = added.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            
        if carryOver > 0:
            added.next = ListNode(carryOver, None)
            
        return head.next
                