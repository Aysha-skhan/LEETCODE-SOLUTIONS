class Solution:
    # space complexity is good but time 32ms
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for k in range(len(magazine)):
            if magazine[k] not in d:
                d[magazine[k]]=1
            else:
                d[magazine[k]]+=1
        for y in range(len(ransomNote)):
            if (ransomNote[y] not in d) or (ransomNote[y] == 0):
                return False
            else:
                ransomNote[y]-=1
        return True
