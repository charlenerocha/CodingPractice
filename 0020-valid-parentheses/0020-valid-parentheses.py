class Solution(object):
    def isValid(self, s):
        seenBrackets = []
        openingBrackets = {"(", "{", "["}
        bracketPairs = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        
        for bracket in s:
            if bracket in openingBrackets:
                seenBrackets.append(bracket)
            elif len(seenBrackets) == 0:
                return False
            elif bracketPairs[bracket] == seenBrackets[-1]:
                seenBrackets.pop()
            else:
                return False
            
        return len(seenBrackets) == 0