class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        l=[]
        for i in range(len(nums)):
            sum+=nums[i]
            l.append(sum)
        return l