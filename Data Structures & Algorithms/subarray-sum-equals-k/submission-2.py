class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        seen = {0: 1}
        total = 0
        for num in nums:
            total += num
            ans += seen.get(total - k, 0)
            seen[total] = seen.get(total, 0) + 1
        return ans