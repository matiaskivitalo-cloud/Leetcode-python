class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one_step_behind = 2
        two_steps_behind = 1

        for i in range(3, n + 1):
            current = one_step_behind + two_steps_behind
            two_steps_behind = one_step_behind
            one_step_behind = current
        
        return one_step_behind