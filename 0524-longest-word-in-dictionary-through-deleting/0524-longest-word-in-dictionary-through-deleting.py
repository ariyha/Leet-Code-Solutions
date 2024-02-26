class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        dictionary.sort(key=lambda x:len(x),reverse=True)

        for i in dictionary:
            if find(s,i):
                return i

        return ""

def find(s,p):
    i=0
    j=0

    while(i<len(s)):
        if s[i]==p[j]:
            j+=1
            if j==len(p):
                return True
        i+=1
    
    return False
