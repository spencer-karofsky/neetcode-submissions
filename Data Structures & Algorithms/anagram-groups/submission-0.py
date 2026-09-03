class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        from collections import defaultdict
        anagrams = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                chars[idx] += 1
            anagrams[tuple(chars)].append(s)
        return list(anagrams.values())