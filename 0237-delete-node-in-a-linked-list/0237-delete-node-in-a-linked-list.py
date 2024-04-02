# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # "steal" the node.next value
        node.val = node.next.val
        
        # recurively call deleteNode on the node after it
        if node.next.next is not None:
            self.deleteNode(node.next)
        else:
            # base case: node.next needs to be disconnected
            node.next = None
        