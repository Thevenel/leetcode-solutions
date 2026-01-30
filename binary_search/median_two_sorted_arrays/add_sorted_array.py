class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sorted_arrays = sorted(nums1 + nums2)
        m = len(sorted_arrays) // 2
        
        if len(sorted_arrays) % 2 == 1:
            return sorted_arrays[m]
        else:
            return (sorted_arrays[m-1] + sorted_arrays[m]) / 2
        
# Example usage:
solution = Solution()
print(solution.findMedianSortedArrays([1,3], [2]))        # Output: 2.0
print(solution.findMedianSortedArrays([1,2], [3,4]))    # Output: 2.5
print(solution.findMedianSortedArrays([0,0], [0,0]))    # Output: 0.0