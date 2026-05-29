# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        pointer = res
        uber = 0
        while True:
            if (l1 == None and l2 == None):
                sum = uber
            elif (l1 == None):
                sum = uber + l2.val
                l2 = l2.next
            elif (l2 == None):
                sum = uber + l1.val
                l1 = l1.next
            else:
                sum = uber + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            uber = 0
            while (sum>9):
                uber += 1
                sum -=10
            pointer.val = sum
            if (uber == 0 and l1 == None and l2 == None):
                break
            else:
                pointer.next = ListNode()
                pointer = pointer.next
        return res