t=INPUT1
s=INPUT2.split('\n')
d={}
for i in s:
    d[i[:3]]=(i[-9:-6],i[-4:-1])
u={'R':1,'L':0}
x='AAA'
i=0
while x!='ZZZ':
    if i>=len(t):t+=t
    x=d[x][u[t[i]]]
    i+=1
print(i)
import math
tt=1
for x in d:
    if x[-1]!='A':continue
    i=0
    while x[-1]!='Z':
        if i>=len(t):t+=t
        x=d[x][u[t[i]]]
        i+=1
    tt=math.lcm(tt,i)
print(tt)
