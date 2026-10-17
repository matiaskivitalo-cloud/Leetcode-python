class Solution:
    def firstUniqChar(self, s: str) -> int:
        memory = {}
        for char in s:
            memory[char] = memory.get(char, 0) + 1
        for i in range(len(s)):
            if memory[s[i]] == 1:
                return i
        return -1