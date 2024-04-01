class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        flg=True
        for i in s:
            if not flg and i!=" ":
                flg=True
                count=0
            if i!=" ":
                count+=1
                continue
            
            flg = False
        
        return count
