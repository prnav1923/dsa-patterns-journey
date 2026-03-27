# Problem: Sliding Window Maximum
# Pattern: Sliding Window

# Approach:
# Use a deque to store the indices of the elements.
# The deque maintains elements in decreasing order.
# The front of the deque will always be the maximum element in the current window.
# Slide the window by adding the new element and removing elements that fall out of the window.

# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # stores *indices*
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
