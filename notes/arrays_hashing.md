# Arrays & Hashing 🧠

The **Arrays & Hashing** pattern is one of the most fundamental techniques in algorithm design. It focuses on using data structures like **Hash Maps** and **Hash Sets** to optimize lookups, frequencies, and existence checks.

## 💡 Pattern Explanation

By trading space for time, we can avoid nested loops (O(n²)) and achieve linear time complexity (**O(n)**).

- **Hash Set**: Used for O(1) existence checks (e.g., finding duplicates).
- **Hash Map**: Used for mapping values to specific data (e.g., value to index, value to frequency). Reductions from O(n) or O(n²) to O(1) lookups are the key strength here.

## 🚀 Common Use Cases

1. Checking for **duplicates** in a collection.
2. Finding **complements** of values (e.g., target - current).
3. Counting **frequencies** of characters or numbers.
4. **Grouping** items by a common property (Anagrams).

---

## 📌 Key Problems

### 1. Two Sum (Easy)
- **Problem**: Given an array `nums` and a `target`, find indices of the two numbers that add up to the target.
- **Why this pattern?**: Instead of checking every pair (O(n²)), we store the "required" number (`target - current`) in a hash map as we iterate.
- **Complexity**:
    - **Time**: O(n) - Single pass through the array.
    - **Space**: O(n) - To store up to `n` elements in the hash map.
- **Cheat Sheet**:
    ```python
    diff = target - n
    if diff in hashmap:
        return [hashmap[diff], i]
    hashmap[n] = i
    ```

---

## ⚡ Pro Tips for Interviews

- **Sort vs. Hash**: Sorting takes O(n log n) but saves space. Hashing takes O(n) time but O(n) space. Always discuss this trade-off.
- **In-place Operations**: If memory is tight, consider if you can use the input array itself as a "pseudo-hashmap" (e.g., marking indices as negative).
- **Early Exits**: In hashing problems, you often find the answer *while* building the map, allowing for an early return.
