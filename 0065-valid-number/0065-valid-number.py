class Solution:
    def isNumber(self, s: str) -> bool:
        def correctSign(checkSign):
            if (checkSign.find('+') == 0 or checkSign.find('+') == -1) and \
               (checkSign.find('-') == 0 or checkSign.find('-') == -1):
                return True
            return False
            
        def isInteger(possible_int):
            if not correctSign(possible_int): return False
            if ('+' in possible_int or '-' in possible_int):
                return len(possible_int) > 1 and possible_int[1:].isdigit()
            return len(possible_int) >= 1 and possible_int.isdigit()
        
        def isDecimal(possible_dec):
            if not correctSign(possible_dec): return False
            
            i = possible_dec.find('.')
            if ('+' in possible_dec or '-' in possible_dec):
                return len(possible_dec) > 2 and ("" == possible_dec[1:i] or possible_dec[1:i].isdigit()) and ("" == possible_dec[i+1:] or possible_dec[i+1:].isdigit())
            return len(possible_dec) > 1 and \
                   ("" == possible_dec[:i] or possible_dec[:i].isdigit()) and ("" == possible_dec[i+1:] or possible_dec[i+1:].isdigit())
    
        if 'e' in s or 'E' in s:
            if s.count('e') > 1 or s.count('E') > 1:
                return False
            
            i = s.find('e')
            if i == -1:
                i = s.find('E')
            
            return self.isNumber(s[:i]) and isInteger(s[i+1:]) and len(s[:i]) > 0 and len(s[i+1:]) > 0
        
        if '.' in s:
            if s.count('.') > 1:
                return False
            return isDecimal(s)
    
        return isInteger(s)