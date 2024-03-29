class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # aaaa aa
        # aaaca aaaaaab
        # canConstructransomNotemagazine canCootemagnstructraninesomNaz
        
        if len(magazine) < len(ransomNote):  return False
        
        magazine_frequency = {}
        ransomNote_frequency = {}
        
        for letter in magazine:
            if magazine_frequency.get(letter):
                magazine_frequency[letter] += 1
            else:
                magazine_frequency[letter] = 1
                
        for letter in ransomNote:
            if not magazine_frequency.get(letter):
                return False
            
            if ransomNote_frequency.get(letter):
                ransomNote_frequency[letter] += 1
            else:
                ransomNote_frequency[letter] = 1
                
        for key, value in ransomNote_frequency.items():
            if not magazine_frequency.get(letter) or magazine_frequency[key] < value:
                return False
            
        return True