def countBits(self, n: int) -> List[int]:
    res=[0,1]
    if n==0 :
        return [0]
    if n==1:
        return res
    for y in range(2,n+1):
        if y%2==0:
            res.append(res[y//2])
        else:
            res.append((res[y//2])+1)
    return res
        
