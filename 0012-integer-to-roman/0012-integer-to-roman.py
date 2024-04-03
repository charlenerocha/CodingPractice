class Solution:
    def intToRoman(self, num: int) -> str:
        symbols_and_values = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50,"L"), (90,"XC"), (100,"C"), (400, "CD"), (500, "D"), (900, "CM"), (1000,"M")]
        
        lowest = len(symbols_and_values)-1
        roman = ""
        while num > 0:
            # choose the roman numeral(s)
            while symbols_and_values[lowest][0] > num:
                lowest -= 1
            
            # subtract that roman numeral from num
            roman += symbols_and_values[lowest][1]
            num -= symbols_and_values[lowest][0]
            
        return roman