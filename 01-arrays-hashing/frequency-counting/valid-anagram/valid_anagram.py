def is_anagram(s: str, t: str) -> bool:
    # Early exit: anagrams must have same length
    if len(s) != len(t):
        return False

    count = {}

    # Count characters in first string
    for i in s:
        count[i] = count.get(i, 0) + 1

    # Decrease counts using second string
    for j in t :
        count[j] = count.get(j,0)-1
    # Check for value gt 0
    for values in count.values() :
        if values != 0 :
                return False
    return True


