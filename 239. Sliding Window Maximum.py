class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s=0
        e=k
        res=[]
        tmp=nums[s:e]
        res.append(max(tmp))
        for k in range(len(nums)-(k)):            
            r=tmp.pop(0)
            tmp.append(nums[e])
            if nums[e]>res[-1]:
                res.append(nums[e])
            else:
                if res[-1] in tmp:
                    res.append(res[-1])
                else:
                    res.append(max(tmp))             
            # res.append(max(tmp))
            # print(tmp)
            e+=1
        return res
        
