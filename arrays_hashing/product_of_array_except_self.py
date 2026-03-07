"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Pattern: Arrays (Prefix & Suffix Products)

Approach: Two-Pass Optimization (O(1) Space)
1. Initialize res array with 1s.
2. Left-to-Right Pass: Update res[i] with the product of all elements to the left (prefix). 
   Update prefix for the next element.
3. Right-to-Left Pass: Multiply res[i] by the product of all elements to the right (postfix).
   Update postfix for the next element.

Time Complexity: O(n)
Space Complexity: O(1) - (Output array is usually not counted)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        
        # Pass 1: Prefix Products
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Postfix Products
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
