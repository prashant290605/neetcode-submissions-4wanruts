# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head
        if fast.next:
            if not fast.next.next:
                return False
        else:
            return False
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                return True
            if fast.next:
                if not fast.next.next:
                    return False
            else:
                return False
        return False