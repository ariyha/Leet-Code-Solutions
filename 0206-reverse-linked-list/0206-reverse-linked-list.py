# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        vals = []
        temp = head
        while(temp):
            vals.append(temp.val)
            temp=temp.next
        temp=head
        for i in range(len(vals)-1,-1,-1):
            temp.val = vals[i]
            temp=temp.next
        return head