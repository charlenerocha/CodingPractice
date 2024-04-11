class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final = []
        freq_to_index = {}
        
        for s in strs:
            freq = str(sorted(s))
            
            # anagrams exist for this string
            if freq in freq_to_index:
                final[freq_to_index[freq]].append(s)
              
            # first of this anagram type
            else:
                final.append([s])
                freq_to_index[freq] = len(final)-1
        
        return final