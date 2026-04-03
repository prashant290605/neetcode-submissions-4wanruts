# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        dummy = ListNode(0)
        l1 = lists[0]
    
        for i in range(1,k):
            new = lists[i]
            node = dummy
            while l1 and new:
                if l1.val <= new.val:
                    node.next = ListNode(l1.val)
                    node = node.next
                    l1 = l1.next
                else:
                    node.next = ListNode(new.val)
                    new = new.next
                    node = node.next
            node.next = l1 or new
            l1 = dummy.next
        return dummy.next

