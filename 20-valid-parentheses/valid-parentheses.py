class Solution:
    def isValid(self, s: str) -> bool:
        r = []
        for x in s:
            if (x == "(" or x == "{" or x == "["):
                r.append(x)
            else:
                if (x == ")"):
                    if (not r or r.pop() != "("):
                        return False 
                if (x == "]"):
                    if (not r or r.pop() != "["):
                        return False
                if (x == "}"):
                    if (not r or r.pop() != "{"):
                        return False
        if r:
            return False
        return True