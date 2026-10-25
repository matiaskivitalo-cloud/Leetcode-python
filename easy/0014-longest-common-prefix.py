class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs:
                if i < len(s) and s[i] == char:
                    continue
                else:
                    return strs[0][:i]
        return strs[0]