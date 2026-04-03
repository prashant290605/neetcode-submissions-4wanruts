# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        second = prev
        first = head
        while second:
            temp1 = first.next if first else None
            temp2 = second.next

            if first:
                first.next = second
            second.next = temp1

            first = temp1
            second = temp2