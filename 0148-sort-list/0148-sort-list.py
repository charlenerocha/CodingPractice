# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1: Convert the linked list into a list of nodes.
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        # Step 2: Sort the list of nodes based on their values.
        nodes.sort(key=lambda x: x.val)
        
        # Step 3: Reconstruct the sorted linked list.
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        # Set the last node's next to None.
        nodes[-1].next = None
        
        return nodes[0]  # Return the new head of the sorted list.
