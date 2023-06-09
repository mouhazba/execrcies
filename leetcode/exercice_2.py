"""
Return the head of the linked list after swapping the values of the kth node
from the beginning and the kth node from
the end (the list is 1-indexed).

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100

example-1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]

example-2:
    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        j = len(head) - k
        i = k-1
        n = len(head)
        if n < 100000:
            if 1 <= k <=n:
                val_1 = head[i]
                val_2 = head[j]
                a[i] = val_2
                a[j] = val_1

        return head

a = [7,9,6,5]
s = Solution()
response = s.swapNodes(a,2)
print(response)
