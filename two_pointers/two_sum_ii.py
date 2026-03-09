"""
Problem: Two Sum II - Input Array Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-sorted/

Pattern: Two Pointers (Optimal for sorted arrays)

Approach 1: Hash Map (O(n) Time, O(n) Space)
Standard Two Sum approach using a dictionary to store complements.

Approach 2: Two Pointers (O(n) Time, O(1) Space)
Since the array is sorted, use a left pointer (start) and right pointer (end).
- If sum > target, move right pointer left.
- If sum < target, move left pointer right.

Time Complexity: O(n)
Space Complexity: O(1) for Two Pointers
"""

class Solution:
    def twoSum_TwoPointers(self, numbers: list[int], target: int) -> list[int]:
        # Optimal approach for sorted arrays
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1] # 1-indexed
        
        return []

    def twoSum_HashMap(self, numbers: list[int], target: int) -> list[int]:
        # Standard approach (works but less space efficient than two pointers here)
        prevMap = {} # val : index

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff] + 1, i + 1]
            prevMap[n] = i
        
        return []
