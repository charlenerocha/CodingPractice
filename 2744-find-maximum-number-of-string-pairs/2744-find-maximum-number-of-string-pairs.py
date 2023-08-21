class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        seen_words = set()
        pairs = 0
        
        for word in words:
            word = frozenset(word)
            if word not in seen_words:
                seen_words.add(word)
            else:
                pairs += 1
                
        return pairs