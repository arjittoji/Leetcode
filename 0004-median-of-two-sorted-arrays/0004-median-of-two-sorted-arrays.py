class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l=len(nums1)
        if l%2!=0:
            return round(nums1[(l-1)//2],5)
        else:
            return round(((nums1[(l-1)//2]+nums1[(l-1)//2+1])/2),5)