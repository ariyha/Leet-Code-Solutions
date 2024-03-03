# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for i in range(n):
            fast = fast.next
       
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next

    #     if(self.findlen(head)==n):
    #         head=head.next
    #         return head

    #     length = self.findlen(head)
    #     temp=head
    #     head1 = head
    #     for i in range(length-n-1):
    #         temp=temp.next

    #     print(temp.val)
    #     if(length==n and n==1):
    #         head=None
    #         return head
    #     temp1 = temp.next
    #     print(temp.next)
    #     try:
    #         print(temp1.next)
    #     except(AttributeError):
    #         pass

    #     try:
    #         temp.next=temp1.next
    #     except(AttributeError):
    #         pass

    #     return head


    # def findlen(self,head):
    #     temp = head
    #     len=0

    #     while(temp!=None):
    #         temp=temp.next
    #         len+=1
        
    #     return len