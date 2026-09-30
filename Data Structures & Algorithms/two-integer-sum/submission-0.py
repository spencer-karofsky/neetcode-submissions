class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}
        for i, num in enumerate(nums):
            if target - num in remaining:
                return [remaining[target - num], i]
            remaining[num] = i