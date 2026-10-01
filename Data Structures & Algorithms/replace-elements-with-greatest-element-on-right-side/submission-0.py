class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_right = [-1]
        max_element = -1
        for i in range(len(arr) - 1, 0, -1):
            max_element = max(max_element, arr[i])
            greatest_right.append(max_element)
        return greatest_right[::-1]