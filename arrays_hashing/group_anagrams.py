"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/

Pattern: Arrays & Hashing

Approach: Hash Map with Frequency Array
Use a hash map where the key is a tuple representing the character count (size 26) of each word.
This avoids sorting O(n log n) and achieves O(m * n) where m is number of strings and n is avg length.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Using defaultdict(list) to handle new keys automatically
        res = defaultdict(list)

        for s in strs:
            # Count array for characters 'a' through 'z'
            count = [0] * 26 
            
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Map the count array to the string
            # list cannot be a key, so we convert it to a tuple
            res[tuple(count)].append(s)
            
        return list(res.values())
