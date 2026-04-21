class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2
        merged.sort()

        totalLength = len(merged)
        if totalLength % 2 == 0: 
            return (merged[totalLength // 2 -1] + merged[totalLength // 2]) / 2.0
        else: 
            return merged[totalLength // 2]