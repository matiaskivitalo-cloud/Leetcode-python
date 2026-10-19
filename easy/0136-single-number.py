class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        memory = {}
        for i in range(len(nums)):
            memory[nums[i]] = memory.get(nums[i], 0) + 1
        for key, value in memory.items():
            if value == 1:
                return key
        