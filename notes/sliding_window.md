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

### 4. Permutation in String (Medium)
- **Problem**: Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.
- **Why this pattern?**: Use a fixed-size sliding window of length `len(s1)`. Maintain an array or hash map of the character frequencies for `s1` and the current window in `s2`. Instead of checking hash maps every time, you can optimize by tracking `matches` (number of characters with identical frequencies).
- **Complexity**:
    - **Time**: $O(N)$ - Where $N$ is the length of `s2`. We do constant work for each slide.
    - **Space**: $O(1)$ - Constant space since we only store frequency counts for 26 lowercase English letters.
- **Cheat Sheet**:
    ```python
    if len(s1) > len(s2): return False
    s1Count, s2Count = [0]*26, [0]*26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
    matches = 0
    for i in range(26):
        if s1Count[i] == s2Count[i]: matches += 1
    
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True
        
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]: matches += 1
        elif s1Count[index] + 1 == s2Count[index]: matches -= 1
        
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]: matches += 1
        elif s1Count[index] - 1 == s2Count[index]: matches -= 1
        l += 1
    return matches == 26
    ```

### 5. Minimum Window Substring (Hard)
- **Problem**: Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.
- **Why this pattern?**: Use a variable sliding window. Maintain two hashmaps: one for characters in `t` (`countT`) and one for the current window (`window`). Track `have` (the number of unique characters that meet the required frequency) and `need` (the total number of unique characters required). Expand the right pointer `r` until `have == need`, then shrink the left pointer `l` to minimize the window while keeping it valid.
- **Complexity**:
    - **Time**: $O(M + N)$ - Where $M, N$ are the lengths of `s` and `t`. Both pointers move from left to right at most once.
    - **Space**: $O(M + N)$ - Space for storing character frequencies in the hashmaps.
- **Cheat Sheet**:
    ```python
    if not t: return ""
    countT, window = {}, {}
    for c in t: countT[c] = 1 + countT.get(c, 0)
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
                resLen = r - l + 1
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if resLen != float("infinity") else ""
    ```

---

## ⚡ Pro Tips for Interviews

- **Identify the Window**: Does the problem involve a contiguous subarray or substring?
- **Pointers**: Usually `l` (left) and `r` (right) are initialized at the start.
- **Optimization**: Sliding window reduces $O(N^2)$ brute force to $O(N)$ or $O(N \log N)$ in some cases.
