# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        max_sum = 0
        i, j = 0, len(arr) - 1
        while i < j:
            twin_sum = arr[i] + arr[j]
            max_sum = max(max_sum, twin_sum)
            i += 1
            j -= 1
        return max_sum

