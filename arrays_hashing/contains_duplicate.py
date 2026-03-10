"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Pattern: Arrays & Hashing

Approach 1: Hash Set (Optimal)
Use a set to store visited numbers. If a number is already in the set, a duplicate exists.

Approach 2: Sorting (Space Optimized)
Sort the array and check adjacent elements for equality.

Time Complexity: O(n) for Approach 1, O(n log n) for Approach 2
Space Complexity: O(n) for Approach 1, O(1) or O(n) for Approach 2 depending on sort implementation
"""

class Solution:
    def containsDuplicate_Set(self, nums: list[int]) -> bool:
        # Approach 1: Using a Hash Set
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    def containsDuplicate_Len(self, nums: list[int]) -> bool:
        # One-liner version of Approach 1
        return len(nums) != len(set(nums))

