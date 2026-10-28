class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        parts = s.strip().split()
        return len(parts[-1])