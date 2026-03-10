"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/

Pattern: Two Pointers (Opposite Directions)

Approach: Two Pointers Optimization (O(1) Space)
1. Clean the string (optional) or move pointers while skipping non-alphanumeric characters.
2. Compare characters at left and right pointers.
3. If they don't match, it's not a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric from left
            while l < r and not self.alphanum(s[l]):
                l += 1
            # Skip non-alphanumeric from right
            while r > l and not self.alphanum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
            
        return True

    def alphanum(self, c: str) -> bool:
        # Custom check for alphanumeric characters
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
