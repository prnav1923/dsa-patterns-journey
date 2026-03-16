"""
Problem: Permutation in String
Pattern: Sliding Window

Approach:
Use a fixed size sliding window of length s1. Maintain a frequency map (or array of 26 characters) for s1 and the current window in s2.
Slide the window across s2, updating the window frequency map. Compare the two frequency maps; if they match, s1's permutation is in s2.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1

        for l in range(len(s2) - len(s1)):
            if matches == 26:
                return True

            r = l + len(s1)
            # Add new character to window
            index = ord(s2[r]) - ord('a')
            window_count[index] += 1
            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] + 1:
                matches -= 1

            # Remove old character from window
            index = ord(s2[l]) - ord('a')
            window_count[index] -= 1
            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] - 1:
                matches -= 1

        return matches == 26
