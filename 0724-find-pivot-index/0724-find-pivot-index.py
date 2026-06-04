class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Tsum=sum(nums)
        lsum,rsum=0,0
        for i in range(len(nums)):
            rsum=Tsum-lsum-nums[i]
            if lsum == rsum:
                return i
            lsum+=nums[i]
        return -1
