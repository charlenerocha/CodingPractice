class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backTrack(finalList, used, path):
            if len(path)==len(nums):
                finalList.append(path[:])
                return
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i]=True
                path.append(num)
                backTrack(finalList, used, path)
                path.pop()
                used[i]=False
        
        final=[]
        backTrack(final, [False]*len(nums), [])
        return final
            