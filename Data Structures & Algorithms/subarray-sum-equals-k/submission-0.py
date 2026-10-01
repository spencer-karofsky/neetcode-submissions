class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 0
        seen = {0: 1}

        for num in nums:
            total += num
            ans += seen.get(total - k, 0)
            seen[total] = seen.get(total, 0) + 1
        return ans
            