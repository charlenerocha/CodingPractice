class Solution(object):
    def isValid(self, s):
        stack=[]

        for i in s:
            if i=='(':
                stack.append(')')
            elif i=='[':
                stack.append(']')
            elif i=='{':
                stack.append('}')
            elif not stack:
                return False
            elif i!=stack[-1]:
                return False
            else:
                stack.pop()
        
        return not stack