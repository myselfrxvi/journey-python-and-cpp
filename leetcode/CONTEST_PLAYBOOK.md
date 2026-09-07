# LeetCode Contest Playbook: Instant Logic Decoder

## 1. The Constraint Speed Limit Rule

Look at `N` (the length of the array or string):

- **If N <= 20:**
  - Allowed time: O(2^N) or O(N!)
  - The answer is **Backtracking** (exhaustive search) or **Bitmasking**.

- **If N <= 1,000:**
  - Allowed time: O(N^2)
  - You can use **two nested loops** or **2D Dynamic Programming**.

- **If N is 100,000 or bigger (Most Common!):**
  - Allowed time: O(N) or O(N log N)
  - Nested loops will FAIL (Time Limit Exceeded).
  - You **MUST** use:
    - **Hash Map** / Hash Set
    - **Two Pointers**
    - **Sliding Window**
    - **Sorting** or **Heap**

- **If N is 1,000,000,000 (1 billion):**
  - Allowed time: O(log N) or O(1)
  - The answer is **Binary Search on Answer** or **Pure Math**.

---

## 2. Trigger Phrases to Algorithm

- **"Contiguous subarray" + "longest" / "shortest":**
  - Pattern: **Sliding Window**

- **"Find a pair of numbers":**
  - If array is sorted: **Two Pointers**
  - If array is not sorted: **Hash Map**

- **"Top K elements" or "K most frequent":**
  - Pattern: **Heap (Priority Queue)**

- **"Next greater number" or "daily temperatures":**
  - Pattern: **Monotonic Stack**

- **"Number of ways to reach..." or "Minimum cost":**
  - Pattern: **Dynamic Programming**

- **"Find all valid arrangements":**
  - Pattern: **Backtracking**
