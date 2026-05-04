class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for word in strs:
            if not res:
                res.append([word])
            else:
                tr = 0
                for liste in res:
                    if isAnagram(self, liste[0], word):
                        liste.append(word)
                        tr += 1
                if tr == 0:
                    res.append([word])
        return res


def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        for x in s:
            if (x not in t):
                return False
            else:
                t = t.replace(x, "", 1)
        return True 