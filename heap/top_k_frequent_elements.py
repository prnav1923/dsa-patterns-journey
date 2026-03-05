"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/

Pattern: Heap / Bucket Sort (Arrays & Hashing optimization)

Approach: Bucket Sort (Optimal O(n))
1. Count frequencies using a hash map.
2. Create a 'freq' list of lists where index is the frequency.
3. Fill 'freq' such that freq[i] contains numbers that appear 'i' times.
4. Iterate backwards from the highest possible frequency to 1, collecting elements until k is reached.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequency (HashMap)
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Bucket Sort approach
        # Index of freq is the frequency of the numbers inside the list
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: Result collection (Iterate desc)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res
