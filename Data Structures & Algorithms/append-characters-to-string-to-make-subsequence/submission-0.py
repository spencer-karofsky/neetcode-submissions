class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_i = 0

        for char in s:
            if t_i < len(t) and t[t_i] == char:
                t_i += 1
        return len(t) - t_i