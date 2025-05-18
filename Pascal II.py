def getRow(self, rowIndex: int) -> List[int]:
    t=[[]]
    for n in range(rowIndex+1):
        if n==0:
            t[0]+=[1]
        elif n==1:
            t.append([1,1])
        else:
            tmp=[1]
            for y in range((len(t[-1]))-1):
                tmp+=[t[-1][y]+t[-1][y+1]]
            tmp+=[1]
            t+=[tmp]
    return t[-1]
