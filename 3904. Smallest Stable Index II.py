class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxx=[]
        curr=0
        for i in range(len(nums)):
            if nums[i]>curr:
                curr=nums[i]
            maxx.append(curr)
        minn=[]
        curr=float('inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<curr:
                curr=nums[i]
            minn.append(curr)
        minn=minn[::-1]
        for m in range(len(maxx)):
            if maxx[m]-minn[m]<=k:
                return m
        return -1


        
