class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_freq = {0: 1} # prefix sum of 0 seen once (default)
        prefix = 0
        for num in nums:
            prefix += num
            answer += prefix_freq.get(prefix - k, 0)
            prefix_freq[prefix] = prefix_freq.get(prefix, 0) + 1
        return answer