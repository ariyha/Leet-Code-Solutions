class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','i','o','u']
        yep = [0]*(len(words)+1)
        score = 0
        for j,i in enumerate(words):
            if i[0] in vowels and i[-1] in vowels:
                score+=1
            yep[j+1]=score

        re = [0]*len(queries)
        for j,i in enumerate(queries):
            l,r = i[0],i[1]
            re[j] = yep[r+1]-yep[l]
        return re