"""
Problem: 3Sum
Link: https://leetcode.com/problems/3sum/

Pattern: Two Pointers (on sorted array)

Approach: O(n^2)
1. Sort the input array.
2. Iterate through the array, treating each element as a potential first element of a triplet.
3. Skip duplicate elements for the first position.
4. Use Two Pointers (left and right) to find pairs that sum to -element.
5. Skip duplicates for left and right pointers when a triplet is found.

Time Complexity: O(n^2)
Space Complexity: O(1) or O(n) depending on the library sort implementation.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # Skip the same value for the first element
            if i > 0 and a == nums[i-1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # Skip duplicates for the second element
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
