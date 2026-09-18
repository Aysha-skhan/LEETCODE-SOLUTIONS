class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        f=0
        l=len(s)-1
        v=['a','e','i','o','u','A','E','I','O','U']
        while f<l:
            if (s[f] in v) and (s[l] in v):
                s[f],s[l]=s[l],s[f]
                l-=1
                f+=1
            elif s[f] not in v and s[l] in v:
                f+=1
            elif s[f] in v and s[l] not in v:
                l-=1
            else:
                l-=1
                f+=1
        res=''
        for k in range(len(s)):
            res+=s[k]
        return res

            
        
