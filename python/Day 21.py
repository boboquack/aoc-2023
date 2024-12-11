s=INPUT.split()
#s='''... .S. ...'''.split()
w=len(s)
h=len(s[0])
w+=2
h+=2
s=['^'*w]+['<'+i+'>' for i in s]+['v'*w]
for i in range(h):
    for j in range(w):
        if s[i][j]=='S':
            s[i]=s[i][:j]+'.'+s[i][j+1:]
            break
    else:continue
    break
r,c=i,j
t={(i,j)}
o=[(0,1),(0,-1),(1,0),(-1,0)]
for i in range(64):
    u=set()
    for i,j in t:
        for di,dj in o:
            if s[i+di][j+dj]=='.':u.add((i+di,j+dj))
    t=u
print(len(t))
'''
t={(r,c,0,0)}
o=[(0,1),(0,-1),(1,0),(-1,0)]
vis={(0,0)}
for z in range(26501365):
    u=set()
    for i,j,ii,jj in t:
        for di,dj in o:
            if s[i+di][j+dj]=='.':u.add((i+di,j+dj,ii,jj))
            if s[i+di][j+dj]=='<':u.add((i+di,w-2,ii,jj-1))
            if s[i+di][j+dj]=='>':u.add((i+di,1,ii,jj+1))
            if s[i+di][j+dj]=='^':u.add((h-2,j+dj,ii-1,jj))
            if s[i+di][j+dj]=='v':u.add((1,j+dj,ii+1,jj))
    for i,j,ii,jj in u:
        if (ii,jj) not in vis:print(z+1,i,j,ii,jj)
    for i,j,ii,jj in u:
        if (ii,jj) not in vis:vis.add((ii,jj))
    t=u
print(len(t))
'''

M=w//2
abs=lambda t:t-1 if t>0 else -t-1
def access(ii,jj):
    if ii==0 and jj==0:return (0,r,c)
    if ii==0 and jj<0:return (M+(w-2)*abs(jj),M,w-2)
    if ii==0 and jj>0:return (M+(w-2)*abs(jj),M,1)
    if ii>0 and jj==0:return (M+(w-2)*abs(ii),1,M)
    if ii<0 and jj==0:return (M+(w-2)*abs(ii),w-2,M)
    if ii>0 and jj>0:return (M*2+(w-2)*abs(jj)+(w-2)*abs(ii),1,1)
    if ii<0 and jj<0:return (M*2+(w-2)*abs(jj)+(w-2)*abs(ii),w-2,w-2)
    if ii>0 and jj<0:return (M*2+(w-2)*abs(jj)+(w-2)*abs(ii),1,w-2)
    if ii<0 and jj>0:return (M*2+(w-2)*abs(jj)+(w-2)*abs(ii),w-2,1)

N=26501365
#N=20
def find(ii,jj):
    (t,i,j)=access(ii,jj)
    if t>N:return 0,False
    u={(i,j)}
    d={}
    while t<N:
        t+=1
        v=set()
        for i,j in u:
            for di,dj in o:
                if s[i+di][j+dj]=='.':v.add((i+di,j+dj))
        d[t]=len(v)
        u=v
        if (t-N)%2==0 and t-2 in d and d[t]==d[t-2]:
            return d[t],True
    return len(u),False

odd=find(0,1)[0]
even=find(0,2)[0]

edge=N//(w-2)+2
t=even

i=0
assert find(edge,0)[0]==0
while not (a:=find(edge-i,0))[1]:
    a=a[0]
    t+=a
    i+=1
x=edge-i
t+=x//2*even
t+=(x+1)//2*odd

i=0
assert find(-edge,0)[0]==0
while not (a:=find(i-edge,0))[1]:
    a=a[0]
    t+=a
    i+=1
x=edge-i
t+=x//2*even
t+=(x+1)//2*odd

i=0
assert find(0,edge)[0]==0
while not (a:=find(0,edge-i))[1]:
    a=a[0]
    t+=a
    i+=1
x=edge-i
t+=x//2*even
t+=(x+1)//2*odd

i=0
assert find(0,-edge)[0]==0
while not (a:=find(0,i-edge))[1]:
    a=a[0]
    t+=a
    i+=1
x=edge-i
t+=x//2*even
t+=(x+1)//2*odd
    
i=0
assert find(edge,1)[0]==0
while not (a:=find(edge-i,1))[1]:
    a=a[0]
    t+=a*(edge-i)
    i+=1
x=edge-i
t+=(x//2)*(x//2+1)*odd
t+=(x*(x+1)//2-(x//2)*(x//2+1))*even

i=0
assert find(edge,-1)[0]==0
while not (a:=find(edge-i,-1))[1]:
    a=a[0]
    t+=a*(edge-i)
    i+=1
x=edge-i
t+=(x//2)*(x//2+1)*odd
t+=(x*(x+1)//2-(x//2)*(x//2+1))*even

i=0
assert find(-edge,1)[0]==0
while not (a:=find(i-edge,1))[1]:
    a=a[0]
    t+=a*(edge-i)
    i+=1
x=edge-i
t+=(x//2)*(x//2+1)*odd
t+=(x*(x+1)//2-(x//2)*(x//2+1))*even

i=0
assert find(-edge,-1)[0]==0
while not (a:=find(i-edge,-1))[1]:
    a=a[0]
    t+=a*(edge-i)
    i+=1
x=edge-i
t+=(x//2)*(x//2+1)*odd
t+=(x*(x+1)//2-(x//2)*(x//2+1))*even

print(t)
