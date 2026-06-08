class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_sorted=sorted(heights)
        count=0
        for i in range(len(heights)):
            if height_sorted[i] != heights[i]: 
                count+=1
        return count
        