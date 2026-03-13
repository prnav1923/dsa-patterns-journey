"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Pattern: Arrays & Hashing

Approach:
Use a hashmap to store visited numbers and their indices.
For each element, check if (target - current number) exists in the hashmap.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[n] = i