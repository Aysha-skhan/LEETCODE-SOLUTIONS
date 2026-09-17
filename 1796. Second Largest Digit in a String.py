class Solution:
    def secondHighest(self, s: str) -> int:
        s=list(s)
        sett=set()
        for k in range(len(s)):
            try:
                sett.add(int(s[k]))
            except:
                pass
        if len(sett)>=1:
            maxx1=max(sett)
            sett.remove(maxx1)
            if len(sett)>=1:
                return max(sett)
            else:
                return -1
        else:
            return -1
