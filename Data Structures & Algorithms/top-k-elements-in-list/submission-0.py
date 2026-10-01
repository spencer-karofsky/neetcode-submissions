class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        c = Counter(nums)
        most_freq = c.most_common(k)
        return [freq[0] for freq in most_freq]