# The Complete Big-O Complexity Roadmap

This roadmap is your blueprint to mastering time and space complexity. By the end of these 6 modules, you will be able to calculate the complexity of any code in 5 seconds and instantly know which algorithm to pick for any LeetCode constraint.

---

## Module 1: The Foundations (O(1) vs O(N))

### What You Will Master:
- **O(1) - Constant Time:** Operations that take the exact same amount of time regardless of data size.
  - Examples: `arr[i]`, `hash_table[key]`, `arr.append(x)`, basic arithmetic `a + b`.
- **O(N) - Linear Time:** Operations that scale directly with data size.
  - Examples: `for x in arr:`, `sum(arr)`, `min(arr)`, `max(arr)`, `arr.index(x)`.

### Key Trap to Watch Out For:
- `x in my_list` is **O(N)** (it scans the whole list).
- `x in my_set` is **O(1)** (instant hash table lookup).
- Replacing a list search with a set search can speed up your code by 10,000x!

---

## Module 2: The Powers of Two (O(log N) vs O(N log N))

### What You Will Master:
- **O(log N) - Logarithmic Time (Cutting in Half):**
  - Any loop that cuts the problem size in half: `while n > 1: n //= 2`.
  - Binary Search: Searching in a sorted array of 1,000,000 elements takes only 20 steps!
- **O(N log N) - Linearithmic Time (Sorting):**
  - Sorting algorithms (Python's Timsort: `arr.sort()`, `sorted()`).
  - Divide-and-conquer algorithms (Merge Sort, Heap Sort).

### The Golden Rule:
Whenever a problem says the array is **already sorted**, your brain should immediately scream: **O(log N) Binary Search**!

---

## Module 3: Polynomial Growth (O(N^2) vs O(N^3))

### What You Will Master:
- **O(N^2) - Quadratic Time (The Nested Loop):**
  - Comparing every element against every other element:
    ```python
    for i in range(len(nums)):
        for j in range(len(nums)):
            # runs N * N times
    ```
  - When is O(N^2) okay? Only when N <= 1,000.
  - When N = 100,000, N^2 = 10,000,000,000 operations (Guaranteed TLE!).
- **O(N^3) - Cubic Time (Triple Nested Loops):**
  - Checking all triplets: acceptable only when N <= 200.

---

## Module 4: The Danger Zone (O(2^N) vs O(N!))

### What You Will Master:
- **O(2^N) - Exponential Time:**
  - Generating all subsets of a set (e.g. `[1, 2, 3]` has 2^3 = 8 subsets).
  - Un-memoized Fibonacci recursion: `fib(n) = fib(n-1) + fib(n-2)`.
  - Only feasible when N <= 20!
- **O(N!) - Factorial Time:**
  - Generating all permutations of N items.
  - Only feasible when N <= 10.

---

## Module 5: Space Complexity (Auxiliary Memory & The Call Stack)

### What You Will Master:
- **O(1) Space:** Your algorithm only uses a few variables (`low`, `high`, `mid`, `count`). No new arrays.
- **O(N) Space:** Your algorithm allocates a list, set, or dictionary that grows with input size.
- **The Hidden Cost: The Call Stack in Recursion:**
  - If a recursive function recurses N times, it creates N stack frames in RAM!
  - Recursion depth = Space Complexity.

---

## Module 6: Python Built-In Complexity Cheat Sheet

| Operation | List | Set | Dict |
| :--- | :--- | :--- | :--- |
| Access by index `arr[i]` | **O(1)** | N/A | N/A |
| Access by key `d[k]` | N/A | N/A | **O(1)** |
| Search `x in obj` | **O(N)** | **O(1)** | **O(1)** |
| Append `obj.append(x)` | **O(1)** amortized | N/A | N/A |
| Add `obj.add(x)` | N/A | **O(1)** | N/A |
| Insert at front `arr.insert(0, x)` | **O(N)** (slow!) | N/A | N/A |
| Delete/Pop end `arr.pop()` | **O(1)** | N/A | N/A |
| Delete/Pop front `arr.pop(0)` | **O(N)** (slow!) | N/A | N/A |
| Slice `arr[a:b]` | **O(b - a)** | N/A | N/A |
| Sort `sorted(arr)` | **O(N log N)** | N/A | N/A |

---

## Module 7: The Contest Constraint Speed-Limit Decoder

When you open any LeetCode problem, look at `N` first:

| Constraint on N | Expected Time Complexity | Permitted Algorithms |
| :--- | :--- | :--- |
| **N <= 10** | O(N!) or O(2^N) | Backtracking, Permutations |
| **N <= 20** | O(2^N) | Backtracking, Recursion, Bitmask DP |
| **N <= 500** | O(N^3) | 3 nested loops, Floyd-Warshall |
| **N <= 2,000** | O(N^2) | 2 nested loops, 2D Dynamic Programming |
| **N <= 100,000** | O(N log N) or O(N) | Sorting, Binary Search, Two Pointers, Sliding Window, Heap, Hash Map |
| **N >= 1,000,000,000** | O(log N) or O(1) | Binary Search on Answer, Pure Math |
