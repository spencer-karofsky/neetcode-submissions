class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        from collections import Counter
        t_freq = Counter(t)
        seen = {} # char in s: count in substring of s formed by window
        formed = 0

        best = (0, 0, float('inf')) # l, r, r - l + 1

        l = 0
        for r in range(len(s)):
            # add char to seen
            seen[s[r]] = seen.get(s[r], 0) + 1
            
            # check if window is valid substring
            if s[r] in t_freq and seen[s[r]] == t_freq[s[r]]:
                formed += 1
                while formed == len(t_freq):
                    if r - l + 1 < best[2]:
                        best = (l, r, r - l + 1)
                    seen[s[l]] -= 1
                    if s[l] in t_freq and seen[s[l]] < t_freq[s[l]]:
                        formed -= 1
                    l += 1
        
        best_l, best_r, best_len = best
        if best_len < float('inf'):
            return s[best_l:best_r + 1]
        return ''