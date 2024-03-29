class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        seen = []

        for c in s:
            if c in brackets:
                seen.append(brackets[c])
            elif seen and c == seen[-1]:
                seen.pop()
            else:
                return False

        return len(seen) == 0