class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s.lower())
        t=list(t.lower())
        if len(s)!=len(t):
            return False
        for k in range(len(s)):
            if s[k] in t:
                t.remove(s[k])
            else:
                return False
        return True
        
