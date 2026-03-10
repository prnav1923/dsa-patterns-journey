# Two Pointers 🏃‍♂️🏃‍♀️

The **Two Pointers** pattern is powerful for searching pairs or subarrays in a sorted array or linked list. 

## 💡 Pattern Explanation

Instead of using nested loops ($O(N^2)$), we use two variables (pointers) that move through the data structure in a coordinated way, usually meeting in the middle or moving at different speeds.

- **Opposite Directions**: Meeting in the middle (e.g., Two Sum II, Valid Palindrome).
- **Same Direction**: Fast and slow pointers (e.g., Linked List Cycle, Remove Duplicates).

## 🚀 Common Use Cases

1. Finding **sum pairs** in a sorted array.
2. Reversing an array or checking for **palindromes**.
3. **Merging** sorted arrays or linked lists.
4. **Squaring** elements and keeping them sorted.

---

## 📌 Key Problems

### 1. Two Sum II - Input Array Sorted (Medium)
- **Problem**: Find indices of two numbers that add up to a target in a **sorted** array.
- **Why this pattern?**: Sorting gives us a property where increasing the left pointer increases the sum, and decreasing the right pointer decreases the sum.
- **Complexity**:
    - **Time**: $O(N)$ - Single pass.
    - **Space**: $O(1)$ - Only two pointers used.
- **Cheat Sheet**:
    ```python
    l, r = 0, len(nums) - 1
    while l < r:
        curSum = nums[l] + nums[r]
        if curSum > target: r -= 1
        elif curSum < target: l += 1
        else: return [l + 1, r + 1]
    ```

### 2. Valid Palindrome (Easy)
- **Problem**: Check if a string is a palindrome after converting to lowercase and removing non-alphanumeric characters.
- **Why this pattern?**: Use two pointers starting at opposite ends. This avoids extra space used by string reversing or lists.
- **Complexity**:
    - **Time**: $O(N)$ - One pass through the string.
    - **Space**: $O(1)$ - Constant space for pointers.
- **Cheat Sheet**:
    ```python
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): l += 1
        while r > l and not s[r].isalnum(): r -= 1
        if s[l].lower() != s[r].lower(): return False
        l, r = l + 1, r - 1
    return True
    ```

---

## ⚡ Pro Tips for Interviews

- **Sorted?**: If you see "Sorted Array", think **Binary Search** or **Two Pointers** immediately.
- **Space Optimization**: Two Pointers usually optimizes Space Complexity from $O(N)$ (Hash Map) to $O(1)$.
- **Loop Condition**: Be careful with `while l < r` vs `while l <= r`. If the pointers can meet at the same element, use `<=`.
- **Duplicates**: If you need unique results (like 3Sum), remember to skip duplicate elements with `while` loops after incrementing/decrementing.
