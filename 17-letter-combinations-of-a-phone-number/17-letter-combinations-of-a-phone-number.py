class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
        
        numToLetter = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        def backTrack(index, path):
            if len(path) == len(digits):
                allCombos.append(path)
                return
                
            myLetters = numToLetter[digits[index]]
            
            for letter in myLetters:
                backTrack(index + 1, path + letter)
            
        allCombos = []
        backTrack(0, "")
        return allCombos