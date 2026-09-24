class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for k in range(1000):
            s=str(nums[k])
            summ=0
            for m in range(len(s)):
                summ+=int(s[m])            
            if summ==k:
                return k
            if k+1==len(nums):
                return -1
        
