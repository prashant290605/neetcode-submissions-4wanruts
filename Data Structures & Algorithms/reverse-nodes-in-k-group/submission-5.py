# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return
        m = 0
        dummy = head
        while dummy:
            dummy = dummy.next 
            m += 1
        
        n = m//k
        prev = None
        curr = head
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        top = head
        
        for i in range(1,n):
            prev2 = None
            top2 = curr
            for i in range(k):
                temp = curr.next
                curr.next = prev2
                prev2 = curr
                curr = temp
            top.next = prev2
            top = top2
        if curr:
            top.next = curr
        return prev
