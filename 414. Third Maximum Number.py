class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        n=len(nums)
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums)
        else:
            max1=max(nums)
            nums.remove(max1)
            max2=max(nums)
            nums.remove(max2)
            max3=max(nums)
            return max3
