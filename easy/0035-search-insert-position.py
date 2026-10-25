class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        mid = len(nums) // 2
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left