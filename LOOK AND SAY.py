# leetcode
def lookAndSequence(n,s='11'):
    if n==0:
        return s
    else:
        s2=''
        s2+= str(s.count(s[0]))
        return lookAndSequence(n-1,s)
print(lookAndSequence(4))

