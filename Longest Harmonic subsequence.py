def findLHS(nums):
    counts={}
    for a in range(len(nums)):
        if nums[a] not in counts:
            counts[nums[a]]=1
        else:
            counts[nums[a]] += 1
    # print(counts)
    maxx=0
    for key,val in counts.items():
        if key<0:
            # print(counts)
            check=-(abs(key)+1)
            # print(check)
            if check in counts:
                # print('yeah')
                if val+counts[check]>maxx:
                    maxx=val+counts[check]
            if key==-1 and (0 in counts):
                if val+counts[0]>maxx:
                    maxx=val+counts[0]
                    # print(maxx)
        else:
            check=key+1
            # print(check)
            if check in counts:
                # print('yeah')
                if val+counts[check]>maxx:
                    maxx=val+counts[check]
    return maxx

print(findLHS([-1,-1,-1,0,0,1,-2,-2]))
