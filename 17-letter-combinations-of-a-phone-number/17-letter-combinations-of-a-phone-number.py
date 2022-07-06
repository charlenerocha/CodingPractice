class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
        
        
        def backTrack(path, index):
            if len(path) == len(digits):
                combos.append("".join(path))
                return
            
            myLet = myHash[digits[index]]
            
            for letter in myLet:
                path.append(letter)
                backTrack(path, index + 1)
                path.pop()
            
        
        myHash = {}
        myHash['2'] = ['a', 'b', 'c']
        myHash['3'] = ['d', 'e', 'f']
        myHash['4'] = ['g', 'h', 'i']
        myHash['5'] = ['j', 'k', 'l']
        myHash['6'] = ['m', 'n', 'o']
        myHash['7'] = ['p', 'q', 'r', 's']
        myHash['8'] = ['t', 'u', 'v']
        myHash['9'] = ['w', 'x', 'y', 'z']
        
        combos = []
        backTrack([], 0)
        return combos