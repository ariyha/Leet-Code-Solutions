class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','i','o','u']
        yep = [0]
        score = 0
        for j,i in enumerate(words):
            if i[0] in vowels and i[-1] in vowels:
                score+=1
            yep.append(score)

        re = []
        for l,r in queries:
            re.append(yep[r+1]-yep[l])
        return re