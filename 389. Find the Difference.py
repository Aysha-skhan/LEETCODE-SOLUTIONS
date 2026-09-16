class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        for k in range(len(t)):
            if t[k] not in s:
                return t[k]
            else:
                s.remove(t[k])
