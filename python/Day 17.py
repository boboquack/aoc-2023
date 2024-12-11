s=INPUT.split()
h=len(s)
w=len(s[0])
er=h
ec=w
s=[[float('inf')]*(w+2)]+[[float('inf')]+[int(i) for i in j]+[float('inf')] for j in s]+[[float('inf')]*(w+2)]
w+=2
h+=2

import heapq
l=[(0,1,1,'r',0)]
done=set()
d1={'r':(0,1),'l':(0,-1),'u':(-1,0),'d':(1,0)}
d2={'r':'ud','l':'ud','u':'lr','d':'lr'}
while True:
    m,r,c,d,n=heapq.heappop(l)
    dr,dc=d1[d]
    r+=dr
    c+=dc
    m+=s[r][c]
    n+=1
    if r==er and c==ec:
        print(m)
        break
    if (r,c,d,n) in done:continue
    done.add((r,c,d,n))
    for nd in d2[d]:
        heapq.heappush(l,(m,r,c,nd,0))
    if n<3:
        heapq.heappush(l,(m,r,c,d,n))

l=[(0,1,1,'r',0)]
done=set()
while True:
    m,r,c,d,n=heapq.heappop(l)
    dr,dc=d1[d]
    r+=dr
    c+=dc
    m+=s[r][c]
    n+=1
    if r==er and c==ec:
        print(m)
        break
    if (r,c,d,n) in done:continue
    done.add((r,c,d,n))
    if n>=4:
        for nd in d2[d]:
            heapq.heappush(l,(m,r,c,nd,0))
    if n<10:
        heapq.heappush(l,(m,r,c,d,n))
