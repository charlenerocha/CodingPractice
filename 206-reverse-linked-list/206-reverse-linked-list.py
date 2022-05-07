# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        
        hi=ListNode(0, next)

        
        if not head: return None
        if not head.next: return head
        
        hold=ListNode(head.next.val, head.next.next)
        myList=ListNode(head.val)
        
        while hold!=None:
            temp=ListNode(myList.val, myList.next)
            holdNode=ListNode(hold.val, None)
            
            myList=holdNode
            myList.next=temp
            
            hold=hold.next
        
        return myList