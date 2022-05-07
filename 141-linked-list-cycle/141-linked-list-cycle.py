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
        myDic={}
        
        while head!=None:
            temp=ListNode(head.val, head.next)
            if temp.next in myDic:
                return True
            else:
                myDic[temp.next]=temp.val
            
            head=head.next
                
        return False
            