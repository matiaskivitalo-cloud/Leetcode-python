class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        memory = {}
        for i in range(len(nums)):
            memory[nums[i]] = memory.get(nums[i], 0) + 1
        return max(memory, key = memory.get)