class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # maxSize places a capacity on the return str
        maxSize = len(strs[0])
        for str in strs:
            maxSize = min(maxSize, len(str))
        if maxSize == 0:
            return ""
        
        index = 0
        common = ""

        while index < maxSize:
            newCommon = strs[0][index]          # new character addition

            for str in strs:
                if str[index] != newCommon:
                    return common
            
            common = common + newCommon
            index += 1

        return common