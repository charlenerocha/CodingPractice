class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        strs.sort()
        common = strs[0]
        
        for s in range(1, len(strs)):
            newCommon = ""
            myStr = strs[s]
                
            for i in range(min(len(common), len(myStr))):
                if myStr[i] == common[i]:
                    newCommon = newCommon + common[i]
                else:
                    break
            common = newCommon
            
        return common