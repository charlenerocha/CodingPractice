class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        seenStrs = {}
        final = []
        index = 0
        
        for myStr in strs:
            
            myStrSorted = ''.join(sorted(myStr))
            
            if myStrSorted in seenStrs:
                final[seenStrs[myStrSorted]].append(myStr)
            else:
                seenStrs[myStrSorted] = index
                final.append([myStr])
                index += 1
        
        return final