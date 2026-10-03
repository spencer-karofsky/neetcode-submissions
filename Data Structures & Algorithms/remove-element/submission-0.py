class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Use a pointer to track the position for the next non-val element
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k