class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        maxlen = 0
        for i in s:
            if i not in sub:
                sub = sub + i
                if len(sub) > maxlen:
                    maxlen = len(sub)
            else:
                idx = sub.index(i)
                sub = sub[idx+1:]
                sub = sub + i
                if len(sub) > maxlen:
                    maxlen = len(sub)
        return maxlen