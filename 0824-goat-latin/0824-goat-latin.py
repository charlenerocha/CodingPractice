class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        result = []
        
        for i, word in enumerate(sentence):
            # word begins with vowel
            if word[0].lower() in {'a', 'e', 'i', 'o', 'u'}:
                word += 'ma'

            # or consonant
            else:
                word += word[0] + 'ma'
                word = word[1:]
                
            # add 'a' per each index
            word += 'a' * (i+1)
            
            result.append(word)
    
        return ' '.join(result)