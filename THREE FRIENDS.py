t=int(input())
for z in range(t):
    a,b,c=map(int,input().split())
    if a==b and b==c:
        print(0)
    elif a==b or a==c or b==c:
        l=[a,b,c]
        maxx=max(l)
        minn=min(l)
        if maxx-minn==1:
            print(0)
        else:
            l.sort()
            if l.count(maxx)>1:
                l[2]=l[2]-1
                l[1] = l[1] - 1
                l[0] = l[0] + 1
            else:
                l[1] = l[1] + 1
                l[0] = l[0] + 1
                l[2] = l[2] - 1
            print(abs(l[1]-l[0])+abs(l[2]-l[0])+abs(l[1]-l[2]))
    else:
        l = [a, b, c]
        l.sort()
        l[0]=l[0]+1
        l[2]=l[2]-1
        # print(l)
        print(abs(l[1]-l[0])+abs(l[2]-l[0])+abs(l[1]-l[2]))

