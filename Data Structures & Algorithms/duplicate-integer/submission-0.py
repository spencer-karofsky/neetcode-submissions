class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = len(nums)

        return len(set(nums)) < n
