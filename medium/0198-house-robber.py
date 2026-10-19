class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1 = 0
        rob2 = 0
        for i in range(len(nums)):
            new_max = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = new_max
        return rob2