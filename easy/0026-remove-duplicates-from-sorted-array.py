class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 1
        for read in range(1, len(nums)):
            if nums[read - 1] != nums[read]:
                nums[write] = nums[read]
                write += 1
        return write