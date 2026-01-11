#LC-217
# Contains Duplicate

## Problem Summary
Given an integer array, return true if any value appears at least twice.
Return false if all elements are unique.

## Brute Force Approach
- Compare every element with every other element
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Not scalable for large inputs

## Optimized Approach (Hash Set)
- Use a hash set to track previously seen values
- If a value appears again, return true immediately

## Dry Run

### Input
nums = [1, 2, 3, 1]

| Step | Current Value | Seen (Before) | Action | Seen (After) |
|----|----|----|----|----|
| 1 | 1 | {} | add | {1} |
| 2 | 2 | {1} | add | {1,2} |
| 3 | 3 | {1,2} | add | {1,2,3} |
| 4 | 1 | {1,2,3} | duplicate found | return True |

### Input
nums = [1, 2, 3, 4]

No duplicates found → return False

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)

## Key Takeaways

- Hash sets allow O(1) lookups
- Early exit improves real performance
- Presence check does not require full frequency counting

