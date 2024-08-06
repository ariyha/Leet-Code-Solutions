from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        word = list(word)
        nums = Counter(word)
        nums = sorted(nums.items(),key=lambda x:x[1],reverse=True)
        out=0

        print(nums)
        for i in range(len(nums)):
            out = out + nums[i][1]*(i//8 + 1)

        return out