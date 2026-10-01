class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        open1="("
        open2="["
        open3="{"
        openn=[]
        for k in range(len(s)):
            if s[k]==open1 or s[k]==open2 or s[k]==open3:
                openn.append(s[k])
            else:
                if len(openn)>=1:
                    chk=openn.pop()
                    if chk =="(" and s[k]!=")":
                        return False
                    elif chk =="[" and s[k]!="]":
                        return False
                    elif chk =="{" and s[k]!="}":
                        return False
                else:
                    return False
        if len(openn)>=1:
            return False
        else:
            return True

        
