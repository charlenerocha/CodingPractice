class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        wordsUsed = 0
        output = []

        while wordsUsed < len(words):
            # add to the current line until its reached the max
            totalCharLine = 0
            curLine = []
            canAddMore = True

            while canAddMore:
                if wordsUsed < len(words) and totalCharLine + len(words[wordsUsed]) <= maxWidth:
                    curLine.append(words[wordsUsed])
                    totalCharLine = totalCharLine + len(words[wordsUsed]) + 1
                    wordsUsed += 1
                else:
                    canAddMore = False

            # choose left or full justify
            if wordsUsed == len(words) or len(curLine) == 1:
                lastLine = True
            else:
                lastLine = False

            if lastLine:
                # left justify
                str = " ".join(curLine)
                for i in range(maxWidth - len(str)):
                    str = str + " "
                output.append(str)

            else:
                # full justify
                
                # adds one space between each word
                for lineWord in range(0, len(curLine) - 1):
                    curLine[lineWord] = curLine[lineWord] + " "
                
                # character count = totalCharLine
                index = 0
                maxIndex = len(curLine) - 2
                totalCharLine -= 1

                while totalCharLine != maxWidth:
                    curLine[index] = curLine[index] + " "
                    totalCharLine += 1

                    index += 1
                    if index > maxIndex:
                        index = 0

                output.append("".join(curLine))

        return output