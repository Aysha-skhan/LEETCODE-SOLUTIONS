#leetcode medium lvl
def divide( dividend, divisor):
    maxx=2**31 - 1
    neg=0
    if (divisor < 0 and dividend>0):
        neg-=1
        divisor*=-1
    elif (divisor > 0 and dividend<0) :
        neg-=1
        dividend*=-1
    if (dividend//divisor) > maxx:
        ans=maxx
    else:
        ans=dividend//divisor
    if neg<0:
        if ans==maxx and dividend>maxx:
            return -(ans+1)
        return -ans
    else:
        return ans
        

        
