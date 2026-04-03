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
        mid = slow
        curr = mid.next

        mid.next = None

        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        hd = head
        while prev:
            temp1 = hd.next 
            temp2 = prev.next
            hd.next = prev
            prev.next = temp1
            hd = temp1
            prev = temp2
        
        
#find middle element via fast and slow method.
#the middle stays in first half of linked list. separate the two lists i.e
#the ends of the lists should always point to None.
#reverse the second list
#now move one by one till second is None