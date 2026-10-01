class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0

        for char in t:
            # Try to find each character in t in order
            if s_i < len(s) and s[s_i] == char:
                s_i += 1
        return s_i == len(s)
