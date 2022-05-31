class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        start = 0
        output = 0
        visited = {}
        
        for end in range(len(s)):
            if s[end] not in visited:
                output = max(output, end - start + 1)
            else:
                if visited[s[end]] < start:
                    output = max(output, end - start + 1)
                else:
                    start = visited[s[end]] + 1
                
            visited[s[end]] = end
            
        return output