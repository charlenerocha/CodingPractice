"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # make a deep copy of the list
        old_node_to_new_node = {}       # new node and old node pair
        old_pointer = head
        new_pointer = Node(-1)
        new_head = new_pointer
        
        while old_pointer:
            new_pointer.next = Node(old_pointer.val)
            new_pointer = new_pointer.next
            old_node_to_new_node[old_pointer] = new_pointer
            old_pointer = old_pointer.next
            
        new_head = new_head.next
        
        # add random pointers
        old_pointer = head
        new_pointer = new_head
        
        while old_pointer:
            if old_pointer.random:
                new_pointer.random = old_node_to_new_node[old_pointer.random]
            else:
                new_pointer.random = None
            old_pointer = old_pointer.next
            new_pointer = new_pointer.next
        
        return new_head