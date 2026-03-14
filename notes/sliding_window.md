# Sliding Window 🪟

The **Sliding Window** pattern is used to perform a required operation on a specific window size of a given array or linked list, such as finding the longest subarray containing all 1s.

## 💡 Pattern Explanation

Sliding windows can be of **fixed** or **variable** size.
- **Fixed Window**: The window size $K$ is constant. We move the window by one element at a time.
- **Variable Window**: The window size expands or shrinks based on certain conditions (e.g., sum, unique characters).

## 🚀 Common Use Cases

1. Finding the **maximum/minimum sum** of all contiguous subarrays of size $K$.
2. Finding the **longest substring** with $K$ distinct characters.
3. String **anagrams** or permutations.

---

## 📌 Key Problems

### 1. Best Time to Buy and Sell Stock (Easy)
- **Problem**: Find the maximum profit you can achieve by buying on one day and selling on a later day.
- **Why this pattern?**: We use a variable sliding window where the left pointer `l` represents the buying day and the right pointer `r` represents the selling day. If we find a lower price than `prices[l]`, we shift our window start to that day.
- **Complexity**:
    - **Time**: $O(N)$ - Single pass through the array.
    - **Space**: $O(1)$ - Constant space for pointers.
- **Cheat Sheet**:
    ```python
    l, r = 0, 1
    max_p = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p
    ```

### 2. Longest Substring Without Repeating Characters (Medium)
- **Problem**: Find the length of the longest substring without repeating characters.
- **Why this pattern?**: Use a variable sliding window. Expand the right pointer `r` to add characters. If a duplicate is encountered, shrink the window from the left `l` until there are no duplicates.
- **Complexity**:
    - **Time**: $O(N)$ - Each character visited twice at most.
    - **Space**: $O(min(N, M))$ - Where $M$ is alphabet size.
- **Cheat Sheet**:
    ```python
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
    ```

### 3. Longest Repeating Character Replacement (Medium)
- **Problem**: You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times. Return the length of the longest substring containing the same letter you can get.
- **Why this pattern?**: Use a sliding window with a frequency map. The valid window condition is `(window length) - (max frequency count in window) <= k`. If invalid, shrink the window from left `l`.
- **Complexity**:
    - **Time**: $O(N)$ - We traverse the string and update variables.
    - **Space**: $O(1)$ - Because the frequency map has at most 26 keys (uppercase letters).
- **Cheat Sheet**:
    ```python
    count = {}
    res, l, maxf = 0, 0, 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
    ```

---

## ⚡ Pro Tips for Interviews

- **Identify the Window**: Does the problem involve a contiguous subarray or substring?
- **Pointers**: Usually `l` (left) and `r` (right) are initialized at the start.
- **Optimization**: Sliding window reduces $O(N^2)$ brute force to $O(N)$ or $O(N \log N)$ in some cases.
