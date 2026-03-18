"""
Problem: Minimum Window Substring
Pattern: Sliding Window

Approach:
Use a variable sliding window. We maintain a `countT` hashmap for the characters in string `t` and a `window` hashmap for the current window in string `s`.
We track two variables: `have` (number of characters whose frequency in the window matches the frequency in `t`) and `need` (total distinct characters in `t`).
Expand the window by moving the right pointer `r`. When `have == need`, the current window is valid. We then try to shrink the window from the left by moving the `l` pointer to find the minimum length valid window.

Time Complexity: O(M + N) where M is the length of s and N is the length of t.
Space Complexity: O(M + N) for the hashmaps.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
