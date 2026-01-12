# LC-242
# Valid Anagram

## Problem Summary
Given two strings `s` and `t`, return true if `t` is an anagram of `s`.
An anagram uses the same characters with the same frequencies, but order does not matter.

---

## Brute Force Approach
- Sort both strings
- Compare sorted results
- Time Complexity: O(n log n)
- Space Complexity: O(n)
- Inefficient due to sorting overhead

---

## Optimized Approach (Frequency Counting)
- Use a hash map to count characters in the first string
- Decrease counts while iterating through the second string
- If any count becomes negative or a character is missing, return false

---

## Dry Run
s = "anagram"
t = "nagaram"


### Step 1: Build Frequency Map from `s`

| Character | Count |
|---------|------|
| a | 3 |
| n | 1 |
| g | 1 |
| r | 1 |
| m | 1 |

---

### Step 2: Process `t`

| Character | Count Before | Count After | Action |
|---------|-------------|------------|-------|
| n | 1 | 0 | continue |
| a | 3 | 2 | continue |
| g | 1 | 0 | continue |
| a | 2 | 1 | continue |
| r | 1 | 0 | continue |
| a | 1 | 0 | continue |
| m | 1 | 0 | continue |

All counts are zero → return **True**

---

### Input
s = "rat"
t = "car"


- Character `c` not found in frequency map  
→ return **False**

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1) (fixed alphabet), O(n) in general case

---

## Key Takeaways
- Anagrams depend on character frequency, not order
- Hash maps enable linear-time comparison
- Early exits improve real-world performance



