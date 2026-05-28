class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Z0-9]', '', s.upper())
        for i in range (len(s)//2):
            if (s[i] != s[len(s)-1-i]):
                return False
        return True