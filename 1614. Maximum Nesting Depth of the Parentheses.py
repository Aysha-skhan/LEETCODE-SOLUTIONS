class Solution:
    def maxDepth(self, s: str) -> int:
        score=0
        maxx=0
        for k in range(len(s)):
            if s[k]=="(":
                score+=1
                if maxx<score:
                    maxx=score            
            elif s[k]==")":
                score-=1
        return maxx
