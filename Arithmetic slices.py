def numberOfArithmeticSlices(nums):
    if len(nums)<=2:
        return 0
    cnt=0
    extra=[]
    for k in range(len(nums)-2):
        if (nums[k]-nums[k+1])==(nums[k+1]-nums[k+2]):
            extra.append(k)
            chkkk=nums[k+1]
            cnt+=1
        else:
            # print(extra)
            for t in range(len(extra)):
                if chkkk-(extra[t]+2)>=1:
                    cnt+=chkkk-(extra[t]+2)
            extra=[]
    if extra!=[]:
        v=len(nums)-1
        for m in range(len(extra)):
            if v-(extra[m]+2)>=1:
                cnt+=v-(extra[m]+2)

    return cnt

print(numberOfArithmeticSlices([1,2,3,4]))
