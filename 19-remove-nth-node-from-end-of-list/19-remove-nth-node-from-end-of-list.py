# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None: return None
        if head.next==None: return None
        
        follow=ListNode(head.val, head.next);
        counter=0;
        
        #find the length
        while follow!=None:
            counter=counter+1
            follow=follow.next
        
        preIndex=counter-n-1
        if preIndex<0: return head.next
        follow=head;
        
        for i in range(counter):
            if i==preIndex:
                follow.next=follow.next.next
                break
                
            follow=follow.next
            
        return head
        
                