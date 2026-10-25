class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        numerals = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for i in range(len(s)):
            if i + 1 < len(s) and numerals[s[i]] < numerals[s[i + 1]]:
                number -= numerals[s[i]]
            else:
                number += numerals[s[i]]
        return number