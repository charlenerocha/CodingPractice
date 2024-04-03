# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int], l=0, r=-2) -> Optional[TreeNode]:
        if r == -2: 
            r = len(nums)-1
            
        if l > r or l < 0 or r >= len(nums):
            return None
        
        # [0, 1]
        # [0, 1, 2]
        # [0]
        
        mid = (r-l)//2 + l
        root = TreeNode(nums[mid], self.sortedArrayToBST(nums, l, mid-1), self.sortedArrayToBST(nums, mid+1, r))
        
        return root