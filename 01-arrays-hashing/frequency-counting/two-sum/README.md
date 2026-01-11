# Two Sum

## Problem
Find two indices such that nums[i] + nums[j] = target.

## Brute Force Approach
- Check all pairs
- Time: O(n²)
- Space: O(1)

## Optimized Approach (Frequency Counting)
- Store visited numbers in a hash map
- Check complement before inserting

## Dry Run
nums = [2, 7, 11, 15], target = 9

Iteration 1:
- num = 2
- complement = 7
- map = {}

Iteration 2:
- num = 7
- complement = 2
- found → return [0, 1]

## Complexity
- Time: O(n)
- Space: O(n)

## Key Takeaways
- Hash maps enable constant-time lookups
- “Check before insert” is reusable across problems

