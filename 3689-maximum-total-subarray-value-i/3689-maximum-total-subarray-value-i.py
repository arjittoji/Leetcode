class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        value  = max(nums) - min(nums)
        return value*k

        