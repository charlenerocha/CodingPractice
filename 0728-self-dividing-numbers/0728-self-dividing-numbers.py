class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            for digit in num:
                if digit == '0' or int(num) % int(digit) != 0:
                    return False
            return True
            
        return [k for k in range(left,right+1) if isSelfDividing(str(k))]