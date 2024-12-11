def isPalindrome(self, x: int) -> bool:
        s=str(x)
        # print(s)
        stk=[]
        for z in range(len(s)):
            stk.append(s[z])
        for m in range(len(s)):
            v=stk.pop()
            if s[m]!=v:
                return False
        return True
