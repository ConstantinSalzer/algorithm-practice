class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range (len(s)):
            x = 0
            y = len(s)-i
            while y <= len(s):
                if self.isPalindrome(s[x:y]):
                    return s[x:y]
                x += 1
                y +=1




    def isPalindrome (self, s: str) -> bool:
        for i in range (len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True