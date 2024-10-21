def asteroidCollision(asteroids):
    pt=-1
    pt2=-2
    for z in range(len(asteroids)-1):
        print(asteroids[pt2],asteroids[pt])
        if (asteroids[pt]<0 and asteroids[pt2]>0) and pt!=0:
            if abs(asteroids[pt])<abs(asteroids[pt2]):
                asteroids.pop(pt)
                if pt!=-1:
                    pt2=pt
                    pt+=1

            elif abs(asteroids[pt])==abs(asteroids[pt2]):
                asteroids.pop(pt)
                asteroids.pop(pt)
                pt+=1
                pt2+=1
            else:
                asteroids.pop(pt2)
        else:
            pt=pt2
            pt2-=1
        if len(asteroids) <= 1:
            break
    return asteroids
asteroids=list(map(int,input().split()))
# print(asteroids)
# print(asteroids[-1])
print(asteroidCollision(asteroids))


