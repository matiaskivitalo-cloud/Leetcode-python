class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memory = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in memory:
                return [memory[diff], i]
                
            memory[nums[i]] = i