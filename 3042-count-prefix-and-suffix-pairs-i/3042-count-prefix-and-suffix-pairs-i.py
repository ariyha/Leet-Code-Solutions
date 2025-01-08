class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            str1 = words[i]
            for j in range(i+1,len(words)):
                str2 = words[j]
                # if len(str1)>len(str2):
                #     continue
                # if str1==str2:
                #     count+=1
                #     continue
                
                # n = len(str1)
                # pref = str2[:n]
                # suff = str2[-n:]

                # if str1==pref and str1==suff:
                #     count+=1
                if words[j].startswith(str1) and words[j].endswith(str1):
                    count+=1
        
        return count