class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        x_string = str(x)
        left = 0
        right = len(x_string) - 1
        while left <= right:
            if x_string[left] != x_string[right]:
                return False
            left += 1
            right -= 1
        return True