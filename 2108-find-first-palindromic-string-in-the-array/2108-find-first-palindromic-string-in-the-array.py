class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if reversed(i)==i:
                return i
            
        return ""