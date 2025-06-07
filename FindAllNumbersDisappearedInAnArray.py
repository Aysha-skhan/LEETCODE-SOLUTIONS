def findDisappearedNumbers(nums):
    res={}
    for y in range(1,len(nums)+1):
        res[y]=0
    for k in range(len(nums)):
        res[nums[k]]+=1 
    arr=[]
    for a in range(1,len(nums)+1):
        if res[a]==0:
            arr.append(a)
    return arr 
        
