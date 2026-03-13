"""
Problem: Longest Substring Without Repeating Characters
Pattern: Sliding Window
LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:
Use a sliding window with two pointers (l, r).
Expand 'r' and store characters in a set.
If a duplicate is found, shrink 'l' until the duplicate is removed.
Track the maximum window size.

Time Complexity: O(n)
Space Complexity: O(min(n, m)) where m is the size of the character set.
"""

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    
    return res

# Example usage:
if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb")) # Output: 3
    print(lengthOfLongestSubstring("bbbbb"))    # Output: 1
    print(lengthOfLongestSubstring("pwwkew"))   # Output: 3
