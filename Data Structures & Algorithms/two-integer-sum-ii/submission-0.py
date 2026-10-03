class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum < target: # increment left
                left += 1
            elif two_sum > target: # decrement right
                right -= 1
            else:
                return [left + 1, right + 1]