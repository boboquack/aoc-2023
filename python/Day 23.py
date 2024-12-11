s=INPUT.split()
ss=SAMPLE.split()
h=len(s)+2
w=len(s[0])+2
s=['#'*w]+['#'+i+'#' for i in s]+['#'*w]

dd={'.':[(0,1),(1,0),(-1,0),(0,-1)],'v':[(1,0)],'^':[(-1,0)],'>':[(0,1)],'<':[(0,-1)],'#':[(0,0)]}
def junc(r,c):
    if s[r][c]!='.':return False
    for dr,dc in dd['.']:
        if s[r+dr][c+dc]=='.':return False
    return True
def ct(r,c):
    z=0
    for dr,dc in dd['.']:
        vr,vc=dd[s[r+dr][c+dc]][0]
        if dr==-vr and dc==-vc:z+=1
    return z
proc=[(1,2,0)]
exp=set()
wait={}
wait2={}
while proc:
    r,c,t=proc.pop()
    u=s[r][c]
    if u=='E':
        print(t)
        break
    if junc(r,c):
        if (r,c) in wait:
            wait[(r,c)]+=1
            wait2[(r,c)]=max(wait2[(r,c)],t)
        else:
            wait[(r,c)]=1
            wait2[(r,c)]=t
        a=wait[(r,c)]
        if a!=ct(r,c):continue
        t=wait2[(r,c)]
    exp.add((r,c))
    for dr,dc in dd[u]:
        if s[r+dr][c+dc]!='#' and (r+dr,c+dc) not in exp:
            proc.append((r+dr,c+dc,t+1))
end=(r,c)
start=(1,2)
edge=set()
proc=[(1,2,1,2,0)]
exp=set()
wait={}
while proc:
    r,c,ir,ic,t=proc.pop()
    u=s[r][c]
    if u=='E':
        edge.add((ir,ic,r,c,t))
        break
    if junc(r,c):
        edge.add((ir,ic,r,c,t))
        if (r,c) in wait:
            wait[(r,c)]+=1
        else:
            wait[(r,c)]=1
        a=wait[(r,c)]
        if a!=ct(r,c):continue
        t=0
        ir=r
        ic=c
    exp.add((r,c))
    for dr,dc in dd[u]:
        if s[r+dr][c+dc]!='#' and (r+dr,c+dc) not in exp:
            proc.append((r+dr,c+dc,ir,ic,t+1))

edges={}
for a,b,c,d,e in edge:
    if (a,b) not in edges:edges[(a,b)]=[]
    edges[(a,b)].append(((c,d),e))
    if (c,d) not in edges:edges[(c,d)]=[]
    edges[(c,d)].append(((a,b),e))

m=0
def dfs(c,v,t):
    global m
    if c==end:
        m=max(m,t)
        return
    v=v|{c}
    for d,k in edges[c]:
        if d not in v:
            dfs(d,v,t+k)
dfs(start,set(),0)
print(m)
