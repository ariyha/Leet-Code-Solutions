class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n<=2:
            return 1
        
        dp =[-1]*(n+1)
        dp[0:3]=[0,1,1]
        def fib(n):
            print(n)
            if dp[n]!= -1:
                return dp[n]
            else:
                dp[n]=fib(n-1)+fib(n-2)+fib(n-3)
                return dp[n]

        return fib(n)