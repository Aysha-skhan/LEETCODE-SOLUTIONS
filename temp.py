class Solution:
    def countCommas(self, n: int) -> int:
        tmp=str(n)
        length=len(tmp)
        if length<=3:
            return 0
        else:
            commas=length//3
            if commas>1 and length%3==0:
                commas-=1
            print(commas, "*", n-999)
            return (commas)*(n-999)

        



