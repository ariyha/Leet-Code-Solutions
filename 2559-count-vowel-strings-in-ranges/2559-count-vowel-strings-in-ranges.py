class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','i','o','u']
        yep = [0]*len(words)
        score = 0
        for j,i in enumerate(words):
            if i[0] in vowels and i[-1] in vowels:
                score+=1
            yep[j]=score

        re = [0]*len(queries)
        for j,i in enumerate(queries):
            l,r = i[0],i[1]
            if l==0:
                re[j]=yep[r]
            else:
                re[j] = yep[r]-yep[l-1]
        return re