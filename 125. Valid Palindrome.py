class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=''
        for k in range(len(s)):
            if (ord(s[k])>=97 and ord(s[k])<=122) or (ord(s[k])>=48 and ord(s[k])<=57):
                n+=s[k]
            elif ord(s[k])>=65 and ord(s[k])<=90:
                n+=(s[k].lower())
        print(n)
        left=0
        right=len(n)-1
        while left < right:
            if n[left]!=n[right]:
                return False
            left+=1
            right-=1
        return True

        
