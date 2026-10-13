class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        memory_s = {}
        memory_t = {}

        for i in range(len(t)):
            memory_s[s[i]] = memory_s.get(s[i],0) + 1
            memory_t[t[i]] = memory_t.get(t[i],0) + 1

        return memory_s == memory_t

            