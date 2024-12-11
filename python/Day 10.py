s=INPUT.split()
h=len(s)
w=len(s[0])
s=[['.']*(w+2)]+[list('.'+i+'.') for i in s]+[['.']*(w+2)]
w+=2
h+=2

dd={'|':'NS','-':'EW','L':'NE','J':'NW','7':'SW','F':'SE','.':'','S':'NSEW'}
o={'N':'S','S':'N','E':'W','W':'E'}
m={'N':(-1,0),'S':(1,0),'E':(0,1),'W':(0,-1)}

for r in range(h):
    for c in range(w):
        if s[r][c]=='S':break
    else:continue
    break

sr=r
sc=c

def move(r,c,d):
    dr,dc=m[d]
    r,c=r+dr,c+dc
    if o[d] not in dd[s[r][c]]:d=None
    else:
        d=list(set(dd[s[r][c]])-{o[d]})[0]
    return r,c,d

for d in 'NSEW':
    di=d
    r,c=sr,sc
    t=0
    while s[r][c]!='S' or t==0:
        r,c,d=move(r,c,d)
        t+=1
        if not d:break
    else:
        print(t//2)
        break

d=di
a=0
tt=0
while s[r][c]!='S' or tt==0:
    if d=='N':a+=c
    if d=='S':a-=c
    r,c,d=move(r,c,d)
    tt+=1
a=abs(a)
print(a-t//2+1)
    
