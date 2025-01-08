class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        for i in range(min(len(v1),len(v2))):
            a,b = int(v1[i]),int(v2[i])
            if a>b:
                return 1
            elif a<b:
                return -1
            j=i+1
        
        if len(v1)==len(v2):
            return 0
        
        if j==len(v1):
            while(j<len(v2)):
                a = int(v2[j])
                if a>0:
                    return -1
                j+=1
        else:
            while(j<len(v1)):
                a = int(v1[j])
                if a>0:
                    return 1
                j+=1

        return 0
