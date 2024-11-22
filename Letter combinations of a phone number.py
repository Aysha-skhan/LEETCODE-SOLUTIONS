def letterCombinations(digits):
    d={1:[],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],
          5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],
          9:['w','x','y','z']}
    if len(digits)==0:
        return []
    if len(digits)==1:
        return d[int(digits[0])]
    else:
        comb=[]
        tmp=d[int(digits[0])]
        for z in range(1,len(digits)):
            tmp_2=d[int(digits[z])]
            for k in range(len(tmp)):
                s = tmp[k] + tmp_2[0]
                comb.append(s)
                s = tmp[k] + tmp_2[1]
                comb.append(s)
                s = tmp[k] + tmp_2[2]
                comb.append(s)
                if len(tmp_2)>3:
                    s = tmp[k] + tmp_2[3]
                    comb.append(s)
            # print(comb)
            tmp=comb[:]
            comb=[]
            # print(tmp,'---tmp---',z)
        return tmp


print(letterCombinations('999'))
# s='abc'
# s2='def'
# s3='ghi'

