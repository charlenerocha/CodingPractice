class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(start, end):
            if start == end or start > end:
                return True
            
            if s[start : (((start + end)//2) + 1)] == s[(((start + end)//2) + (start + end) % 2) : end + 1][::-1]:
                return True
            
        longest = 0
        longestPalindrome = ""
        
        for start in range(len(s)):
            for end in range(start, len(s)):
                if end - start + 1 > longest and isPalindrome(start, end):
                    longest = end - start + 1
                    longestPalindrome = s[start:end + 1]
                    
        return longestPalindrome