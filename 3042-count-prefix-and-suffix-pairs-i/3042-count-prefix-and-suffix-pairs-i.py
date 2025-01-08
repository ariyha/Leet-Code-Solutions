class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            str1 = words[i]
            for j in range(i+1,len(words)):
                if words[j].startswith(str1) and words[j].endswith(str1):
                    count+=1        
        return count