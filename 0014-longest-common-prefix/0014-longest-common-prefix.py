class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        index = 0
        common = ""

        while True:
            if index < len(strs[0]):
                newCommon = strs[0][index]          # new character addition
            else:
                return common

            for str in strs:
                if index >= len(str) or str[index] != newCommon:
                    return common
            
            common = common + newCommon
            index += 1

        return common