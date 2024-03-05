class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1

        while(i<j and s[i]==s[j]):
            cur = s[i]
            while(i<=j and s[i]==cur):
                i+=1
            
            while(i<=j and s[j]==cur):
                j-=1
            
        return j-i+1