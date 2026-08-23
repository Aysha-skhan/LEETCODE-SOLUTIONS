class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for k in range(len(magazine)):
            if magazine[k] not in d:
                d[magazine[k]]=1
            else:
                d[magazine[k]]+=1
        for y in range(len(ransomNote)):
            if (ransomNote[y] not in d) or (d[ransomNote[y]] == 0):
                return False
            else:
                d[ransomNote[y]]-=1
        return True
        
