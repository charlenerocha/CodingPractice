class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            if num in visited:
                return [visited[num], i]
            visited[target - num] = i
        return [-1, -1]