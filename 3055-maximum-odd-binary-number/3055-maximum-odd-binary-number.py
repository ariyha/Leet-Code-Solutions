class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # s = list(s)
        # s.sort(reverse=True)
        # return "".join(s[1:]+['1'])
        flg=True
        k=''
        for i in s:
            if i=='1':
                if flg:
                    flg=False
                    continue
                else:
                    k = '1'+k
            else:
                k=k+'0'
            
        return k+'1'
                
