class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # print(nums)
        s=[]
        for k in range(len(nums)):
            l=k+1
            r=len(nums)-1
            if k>0 and nums[k-1]==nums[k]:
                    continue
            while l<r:
                if nums[l]+nums[r]+nums[k]==0:
                    s.append([nums[k], nums[l], nums[r]])
                    # print(nums[l],"+",nums[r],"=",nums[k])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while r>l and nums[r]==nums[r+1]:
                        r-=1
                elif (nums[l]+nums[r]+nums[k])>0:
                    r-=1
                else:
                    l+=1               
        return s



        
