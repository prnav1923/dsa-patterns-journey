"""
Problem: Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/

Pattern: Greedy / Kadane's Algorithm

Approach: Kadane's Algorithm (O(n))
1. Iterate through the array.
2. Maintain a running sum (curSum).
3. If curSum becomes negative, reset it to 0 (greedy choice: start fresh from the next element).
4. Track the maximum sum encountered so far (maxSub).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0 # Reset if the sum becomes a burden
            curSum += n
            maxSub = max(maxSub, curSum)
            
        return maxSub
