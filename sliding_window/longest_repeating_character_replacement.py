"""
Problem: Longest Repeating Character Replacement
Pattern: Sliding Window
LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement/

Approach:
Use a sliding window (l, r) and a hash map or array to keep track of character frequencies in the current window.
The key insight is: window_len - max_frequency_of_a_single_char_in_window <= k
If this condition holds, it means we can replace all other characters in the window with the most frequent character using at most 'k' replacements.
If the condition doesn't hold, we shrink the window by moving 'l' forward and decrementing the frequency of the character at 'l'.

Time Complexity: O(n)
Space Complexity: O(1) space since we only store frequencies of 26 uppercase English letters.
"""

def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res

# Example usage:
if __name__ == "__main__":
    print(characterReplacement("ABAB", 2)) # Output: 4
    print(characterReplacement("AABABBA", 1)) # Output: 4
