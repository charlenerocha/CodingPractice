class Solution:
    def decodeString(self, s: str) -> str:

        read = []       # tracks the characters read from s

        # repeats the string and adds it to the stack
        def repeatMe(num, toRepeat):
            nonlocal read
            final = []
            for i in range(num):
                read += toRepeat

        # finds the string to repeat and the number of times
        def findContents():
            nonlocal read
            inside = []
            num = ""
            foundBracket = False

            while not foundBracket:
                if read[-1] != "[":
                    inside.append(read.pop())
                else:
                    read.pop()
                    num = read.pop()
                    while len(read) >= 1 and read[-1].isnumeric():
                        num = read.pop() + num
                    foundBracket = True
            inside.reverse()
            repeatMe(int(num), inside)

        index = 0               # iterator
        while index < len(s):
            if s[index] != "]":
                read.append(s[index])
            else:
                findContents()
            index += 1

        return ''.join(read)
