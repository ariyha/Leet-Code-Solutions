class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def dfs(o,c,s):
            if o==c and o==n:
                out.append(s)
            if o<n:
                dfs(o+1,c,s+'(')
            if c<o:
                dfs(o,c+1,s+')')
        
        dfs(0,0,'')

        return out
            
        
