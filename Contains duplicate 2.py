def containsNearbyDuplicate(nums, k):
    dictt={}
    if len(nums)<=1 and k>=1:
        return False
    for y in range(len(nums)):
        if nums[y] in dictt:
            dictt[nums[y]].append(y)
        elif nums[y] not in dictt:
            dictt[nums[y]]=[y]
    for keyy,v in dictt.items():
        if len(v)>1:
            for z in range(len(v)-1):
                chk=abs(v[z]-v[z+1])
                print(chk)
                if chk<=k:
                    return True
    return False

print(containsNearbyDuplicate([1],2))
