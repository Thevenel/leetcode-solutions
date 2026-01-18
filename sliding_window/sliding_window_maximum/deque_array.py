import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            #pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l +=1
            r += 1
        return output

# Example usage:
solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
