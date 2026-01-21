# Best Time to Buy and Sell Stock (LeetCode 121)

## Problem Summary
You are given an array where each element represents the price of a stock on a given day.
You may buy once and sell once. Return the maximum profit possible.

If no profit can be made, return 0.

---

## Brute Force Approach
- Try all possible buy and sell days
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Not scalable

---

## Optimized Approach (Sliding Window / Min Tracking)
- Track the minimum price seen so far
- For each day, calculate profit if sold today
- Update maximum profit accordingly

---

## Dry Run

### Input
prices = [7, 1, 5, 3, 6, 4]


| Day | Price | Min Price So Far | Profit | Max Profit |
|----|------|------------------|--------|------------|
| 1 | 7 | 7 | 0 | 0 |
| 2 | 1 | 1 | 0 | 0 |
| 3 | 5 | 1 | 4 | 4 |
| 4 | 3 | 1 | 2 | 4 |
| 5 | 6 | 1 | 5 | 5 |
| 6 | 4 | 1 | 3 | 5 |

Return **5**

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Takeaways
- Track minimum state while scanning
- Sliding window is implicit
- Greedy decisions with state tracking are powerful

