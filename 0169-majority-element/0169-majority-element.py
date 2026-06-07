class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums):
            z = nums.count(nums[i])
            if z > len(nums)/2:
                return nums[i]
            i+=z
            
            
            

        