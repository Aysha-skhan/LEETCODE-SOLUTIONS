class Solution:
    def mySqrt(self, x: int) -> int:
        chk=x//2
        if x==1:
            return 1
        if x==0:
            return 0
        while chk>0:
            if chk*chk==x:
                return chk
            elif chk*chk>x:
                chk=chk//2
            elif chk*chk<x and ((chk+1)*(chk+1))<=x:
                chk+=1
            elif chk*chk<x and ((chk+1)*(chk+1))>x:
                return chk
