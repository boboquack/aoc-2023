s=INPUT.split()
blocks=[]
for i in s:
    j,k=i.split('~')
    a,b,c=map(int,j.split(','))
    d,e,f=map(int,k.split(','))
    if a==d and b==e and c==f:
        blocks.append(([(a,b,c)],[(a,b,c-1)]))
    elif a!=d:
        blocks.append(([(i,b,c) for i in range(min(a,d),max(a,d)+1)],[(i,b,c-1) for i in range(min(a,d),max(a,d)+1)]))
    elif b!=e:
        blocks.append(([(a,i,c) for i in range(min(b,e),max(b,e)+1)],[(a,i,c-1) for i in range(min(b,e),max(b,e)+1)]))
    else:
        blocks.append(([(a,b,i) for i in range(min(c,f),max(c,f)+1)],[(a,b,min(c,f)-1)]))
snap=[[[0]*1000 for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        snap[i][j][0]=1
for i,j in blocks:
    for a,b,c in i:
        snap[a][b][c]=1
def drop(t):
    i,j=blocks[t]
    blocks[t]=([(a,b,c-1) for a,b,c in i],[(a,b,c-1) for a,b,c in j])
change=True
while change:
    change=False
    for t in range(len(blocks)):
        i,j=blocks[t]
        while all(snap[a][b][c]==0 for a,b,c in j):
            for a,b,c in i:snap[a][b][c]=0
            drop(t)
            i,j=blocks[t]
            for a,b,c in i:snap[a][b][c]=1
            change=True
def copy(l):
    if type(l)==int or type(l)==tuple:return l
    else:return [copy(i) for i in l]
snapt=copy(snap)
blockt=copy(blocks)
z=0
for tt in range(len(blocks)):
    snap=copy(snapt)
    for a,b,c in blocks[tt][0]:snap[a][b][c]=0
    for t in range(len(blocks)):
        if t!=tt:
            i,j=blocks[t]
            if all(snap[a][b][c]==0 for a,b,c in j):
                break
    else:
        z+=1
print(z)
z=0
for tt in range(len(blocks)):
    snap=copy(snapt)
    blocks=copy(blockt)
    for a,b,c in blocks[tt][0]:snap[a][b][c]=0
    d=set()
    change=True
    while change:
        change=False
        for t in range(len(blocks)):
            if t==tt:continue
            i,j=blocks[t]
            while all(snap[a][b][c]==0 for a,b,c in j):
                d.add(t)
                for a,b,c in i:snap[a][b][c]=0
                drop(t)
                i,j=blocks[t]
                for a,b,c in i:snap[a][b][c]=1
                change=True
    z+=len(d)
print(z)
