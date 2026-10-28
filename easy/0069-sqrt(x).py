class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        sqrt = 0
        while left <= right:
            middle = (left + right) // 2
            middle_squared = middle * middle
            if middle_squared > x:
                right = middle - 1
            elif middle_squared < x:
                save = middle
                left = middle + 1
            else:
                return middle
        return save