class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        seen = {0: 1}
        prefix = 0
        for num in nums:
            prefix += num
            rem = prefix % k
            ans += seen.get(rem, 0)
            seen[rem] = seen.get(rem, 0) + 1
        return ans