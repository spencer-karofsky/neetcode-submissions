class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_prod = [1] * n
        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]
        
        right_prod = [1] * n
        for j in range(n - 2, -1, -1):
            right_prod[j] = right_prod[j + 1] * nums[j + 1]
        
        return [l * r for l, r in zip(left_prod, right_prod)]