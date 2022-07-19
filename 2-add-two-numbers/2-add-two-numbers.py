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
        
        first = l1
        second = l2
        
        head = ListNode()
        myList = head
        carryOver = 0
        
        while first or second or carryOver != 0:
            sum = 0
            
            if first:
                sum = first.val
                first = first.next
            if second:
                sum = sum + second.val
                second = second.next
                
            sum = sum + carryOver
            
            myList.next = ListNode(sum % 10, None)
            myList = myList.next
            
            carryOver = sum / 10
            
        return head.next
            