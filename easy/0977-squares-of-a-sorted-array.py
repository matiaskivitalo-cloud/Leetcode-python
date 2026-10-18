class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        new_nums = []
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                new_nums.append(nums[right] ** 2)
                right -= 1
            else:
                new_nums.append(nums[left] ** 2)
                left += 1
        new_nums.reverse()
        return new_nums

