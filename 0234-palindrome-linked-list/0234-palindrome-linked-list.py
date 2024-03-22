class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        k=[]
        while(temp):
            k.append(temp.val)
            temp=temp.next
        return k==k[::-1]