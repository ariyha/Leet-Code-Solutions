class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow=1
        flg=False
        if n<0:
            n=-n
            flg=True

        while(n!=0):
            if n%2!=0:
                pow=pow*x
            x=x*x
            n=int(n/2)
        
        if flg:
            return 1/pow
        else:
            return pow

