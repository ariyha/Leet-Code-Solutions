# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        i = 0
        while(i<n):
            if fast:
                fast = fast.next
                i = i+1
            else:
                break
    

        if i<n:
            return head

        if i == n and not fast:
            return head.next

        slow = head

        while(fast.next):
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head