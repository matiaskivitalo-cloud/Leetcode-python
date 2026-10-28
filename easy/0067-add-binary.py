class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        binary_sum = bin(int_a + int_b)
        return binary_sum[2:]