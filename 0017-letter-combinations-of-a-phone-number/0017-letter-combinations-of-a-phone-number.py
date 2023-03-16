class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        number_to_letter = {   "2" : ["a", "b", "c"],
                               "3" : ["d", "e", "f"],
                               "4" : ["g", "h", "i"],
                               "5" : ["j", "k", "l"],
                               "6" : ["m", "n", "o"],
                               "7" : ["p", "q", "r", "s"],
                               "8" : ["t", "u", "v"],
                               "9" : ["w", "x", "y", "z"]
                           }
        letter_combinations = []
        
        def find_letter_combinations(digits_left, combination):
            if len(digits_left) == 0:
                if len(combination) > 0:
                    letter_combinations.append(combination)
                return
            
            letters_to_add = number_to_letter[digits_left[0]]
            
            for letter_to_add in letters_to_add:
                find_letter_combinations(digits_left[1:], combination + letter_to_add)
            
        
        find_letter_combinations(digits, "")
        
        return letter_combinations