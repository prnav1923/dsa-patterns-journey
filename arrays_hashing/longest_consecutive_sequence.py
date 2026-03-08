"""
Problem: Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Pattern: Arrays & Hashing (Hash Set for Sequence Starting Points)

Approach: Hash Set Optimization (O(n))
1. Convert the input array into a set for O(1) lookups.
2. Iterate through each number in the set.
3. Check if the current number is the start of a sequence (i.e., num - 1 is NOT in the set).
4. If it is a start, keep checking for the next numbers in the sequence (num + 1, num + 2...) and track the length.
5. Update the longest sequence found so far.

Time Complexity: O(n) - Each number is visited at most twice.
Space Complexity: O(n) - To store numbers in a set.
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in numSet:
            # Check if i is the start of a sequence
            if i - 1 not in numSet:
                length = 1
                while i + length in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
