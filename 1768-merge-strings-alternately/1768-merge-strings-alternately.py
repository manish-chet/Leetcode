class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = j = 0
        n, m = len(word1), len(word2)
        
        # Merge characters alternately
        while i < n and j < m:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        
        # Append remaining characters (if any)
        if i < n:
            merged.append(word1[i:])
        if j < m:
            merged.append(word2[j:])
        
        return ''.join(merged)
