class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        iter=0
        dic1={}
        dic2={}
        while True:
            if iter>=len(nums1) and iter>=len(nums2):
                break
            if iter<len(nums1):
                if nums1[iter] in dic1:
                    dic1[nums1[iter]]+=1
                else:
                    dic1[nums1[iter]]=1
            if iter<len(nums2):
                if nums2[iter] in dic2:
                    dic2[nums2[iter]]+=1
                else:
                    dic2[nums2[iter]]=1
            iter+=1
        if len(dic1)>=len(dic2):
            lg=dic1
            sm=dic2
        else:
            sm=dic1
            lg=dic2
        res=[]
        for k,v in lg.items():
            if k in sm:
                if v>sm[k]:
                    v=sm[k]
                for a in range(v):
                    res.append(k)
        return res
        
