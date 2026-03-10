"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Pattern: Two Pointers (Greedy)

Approach: Two Pointers (O(n))
1. Initialize two pointers at the ends of the array.
2. Calculate the area (width * min(height_left, height_right)).
3. Update maxArea if current area is larger.
4. Move the pointer pointing to the shorter height (greedy choice: keep the taller wall for a potential bigger future area).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res
