class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxx=len(nums)
        nums=set(nums)
        for k in range(maxx+1):
            if k not in nums:
                return k
