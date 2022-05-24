class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def backTrack(finalArr, used, path):
            if len(path)==len(nums):
                if path not in finalArr:
                    finalArr.append(path[:])
                return
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i]=True
                path.append(num)
                backTrack(finalArr, used, path)
                used[i]=False
                path.pop()
                
        
        final=[]
        backTrack(final, [False]*len(nums), [])
        return final