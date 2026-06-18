class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        lc = nums.copy()
        lc.reverse()
        return nums+lc
        