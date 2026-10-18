class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        i = 0
        while index < len(s) and i < len(t):
            if t[i] == s[index]:
                index += 1
            i += 1   
        return index == len(s)