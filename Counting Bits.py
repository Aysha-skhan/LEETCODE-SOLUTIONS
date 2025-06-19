def countBits(n):
    #divide again and again by 2 unless 0 or 1 (instead use dp)
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
    
        
