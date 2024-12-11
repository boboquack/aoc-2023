s=INPUT.split('\n\n')
t=s[1].split()
u=s[0].split()
x='x'
m='m'
a='a'
s='s'
tt=[]
for i in t:
    v=i[1:-1].split(',')
    w=[int(i.split('=')[1]) for i in v]
    d={x:w[0],m:w[1],a:w[2],s:w[3]}
    tt.append(d)
t=tt
uu={}
for i in u:
    v=i[:-1].split('{')
    n=v[0]
    v=v[1].split(',')
    uu[n]=v
def ok(e,t):
    if '<' in e:
        lh,rh=e.split('<')
        if t[lh]<int(rh):return True
        return False
    if '>' in e:
        lh,rh=e.split('>')
        if t[lh]>int(rh):return True
        return False
    if '=' in e:
        lh,rh=e.split('=')
        if t[lh]==int(rh):return True
        return False
    raise Exception
u=uu
zz=0
for i in t:
    r='in'
    while r!='R' and r!='A':
        l=u[r]
        for j in l:
            if ':' in j:
                e,n=j.split(':')
                if ok(e,i):
                    r=n
                    break
            else:
                r=j
    if r=='A':zz+=i[x]+i[m]+i[a]+i[s]
print(zz)

def frac(o,e):
    if o==None:return None,None
    oo={i:o[i] for i in o}
    oo2={i:o[i] for i in o}
    oo3={i:o[i] for i in o}
    if '<' in e:
        lh,rh=e.split('<')
        rh=int(rh)
        lo,hi=o[lh]
        if hi<rh:return [oo],[None]
        if lo>=rh:return [None],[oo]
        oo[lh]=(lo,rh-1)
        oo2[lh]=(rh,hi)
        return [oo],[oo2]
    if '>' in e:
        lh,rh=e.split('>')
        rh=int(rh)
        lo,hi=o[lh]
        if lo>rh:return [oo],[None]
        if hi<=rh:return [None],[oo]
        oo[lh]=(rh+1,hi)
        oo2[lh]=(lo,rh)
        return [oo],[oo2]
    if '=' in e:
        lh,rh=e.split('=')
        rh=int(rh)
        lo,hi=o[lh]
        if not lo<=rh<=hi:return [None],[oo]
        if lo==hi==rh:
            return [oo],None
        if lo==rh:
            oo[lh]=(rh,rh)
            oo2[lh]=(rh+1,hi)
            return [oo],[oo2]
        if hi==rh:
            oo[lh]=(rh,rh)
            oo2[lh]=(lo,rh-1)
            return [oo],[oo2]
        oo[lh]=(rh,rh)
        oo2[lh]=(lo,rh-1)
        oo3[lh]=(rh+1,hi)
        return [oo],[oo2,oo3]
    raise Exception
op=[{x:(1,4000),m:(1,4000),a:(1,4000),s:(1,4000)}]
def acc(op,r):
    if r=='R':return []
    if r=='A':return op
    l=u[r]
    v=[]
    for i in l[:-1]:
        i1,i2=i.split(':')
        opp=[frac(o,i1) for o in op]
        opa=[]
        for i in opp:opa+=i[0]
        opr=[]
        for i in opp:opr+=i[1]
        v+=acc(opa,i2)
        op=opr
    v+=acc(opr,l[-1])
    return v
z=0
for d in acc(op,'in'):
    if d!=None:
        z+=(d[x][1]-d[x][0]+1)*\
            (d[m][1]-d[m][0]+1)*\
            (d[a][1]-d[a][0]+1)*\
            (d[s][1]-d[s][0]+1)
print(z)
