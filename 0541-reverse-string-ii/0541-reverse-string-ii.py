class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        i = 0
        l, r = 2*k*i, (2*k*i) + k
        
        while l < len(s):
            s[l:r] = s[l:r][::-1]
            i += 1
            l, r = 2*k*i, (2*k*i) + k 
            
        return "".join(s)