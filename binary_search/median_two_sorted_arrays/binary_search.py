class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2
            
            a_left = A[i] if i >= 0 else float("-infinity")
            a_right = A[i + 1] if (i + 1) < len(A) else float("infinity")
            b_left = B[j] if j >= 0 else float("-infinity")
            b_right = B[j + 1] if (j + 1) < len(B) else "infinity"
            
            # partition is correct
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2 == 1:
                    return min(a_right, b_right)
                #even
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1
                
# Example usage:
solution = Solution()
print(solution.findMedianSortedArrays([1,3], [2]))        # Output: 2.0
print(solution.findMedianSortedArrays([1,2], [3,4]))    # Output: 2.5
print(solution.findMedianSortedArrays([0,0], [0,0]))    # Output: 0.0