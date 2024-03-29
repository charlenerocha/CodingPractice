class Trie:

    def __init__(self, val=0):
        self.val = val
        self.next = []

    def insert(self, word: str) -> None:
        if word == "":
            return self.next.append(Trie("$"))
        
        found = False
        for trie in self.next:
            if trie.val == word[0]:
                trie.insert(word[1:])
                found = True
                break  # Break loop once found matching character
        if not found:
            self.next.append(Trie(word[0]))
            self.next[-1].insert(word[1:])

    def search(self, word: str) -> bool:
        if word == "":
            for trie in self.next:
                if trie.val == "$":
                    return True
            return False
        
        for trie in self.next:
            if trie.val == word[0]:
                return trie.search(word[1:])
        return False
        
    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        
        for trie in self.next:
            if trie.val == prefix[0]:
                return trie.startsWith(prefix[1:])
        return False
