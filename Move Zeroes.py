def moveZeroes(self, nums: List[int]) -> None:
    for y in range(len(nums)):
        if nums[y]==0:
            chk=y+1
            while chk<len(nums):
                if nums[chk]!=0:
                    nums[chk],nums[y]=nums[y],nums[chk]
                    break
                chk+=1
