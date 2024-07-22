class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = list(zip(names,heights))
        a.sort(key=lambda x:x[1],reverse = True)
        out = []
        for i in a:
            out.append(i[0])
        return out