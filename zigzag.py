def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        ans=['']*numRows
        indx = 0
        for k in range(len(s)):
                
            if indx==0:
                flag=True
                # print(ind)
            elif indx==numRows-1:
                flag=False
            if flag:
                ans[indx]+=s[k]
                ind+=1
            else:
                ans[indx] += s[k]
                ind-=1
        answer=''
        for u in range(len(ans)):
            answer+=ans[u]
        return answer
