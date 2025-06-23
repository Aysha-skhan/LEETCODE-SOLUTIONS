def sortColors(self, nums: List[int]):
    for k in range(len(nums)):
        for i in range(k+1,len(nums)):
            if nums[k]>nums[i]:
                nums[k],nums[i]=nums[i],nums[k]
        
#in-place sorting was required
