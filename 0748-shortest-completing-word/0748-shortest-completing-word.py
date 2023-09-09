class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lettersNeeded = Counter(filter(lambda x: x.isalpha(), licensePlate.lower()))
        return min([word for word in words if (Counter(word) & lettersNeeded) == lettersNeeded], key=len)
        