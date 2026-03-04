"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Pattern: Arrays & Hashing

Approach 1: Hash Map (Frequency Counter)
Count the frequency of each character in both strings and compare them.

Approach 2: Sorting
Sort both strings and compare if they are equal.

Time Complexity: O(n) for Approach 1, O(n log n) for Approach 2
Space Complexity: O(k) for Approach 1 (where k is alphabet size), O(1) or O(n) for Approach 2
"""

class Solution:
    def isAnagram_HashMap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

    def isAnagram_Counter(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagram_Sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
