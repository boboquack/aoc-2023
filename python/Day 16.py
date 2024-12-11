s=INPUT.split()
h=len(s)
w=len(s[0])
todo=[(0,0,'R')]
found=set()
dirs={'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)}
corr={'.':{i:i for i in 'RLUD'},
      '\\':{'R':'D','D':'R','L':'U','U':'L'},
      '/':{'R':'U','U':'R','L':'D','D':'L'},
      '|':{'R':'UD','L':'UD','U':'U','D':'D'},
      '-':{'R':'R','L':'L','D':'LR','U':'LR'}}
while todo:
    t=todo.pop()
    r,c,d=t
    if t in found:continue 
    if c<0 or c>=w or r<0 or r>=h:continue
    found.add(t)
    p=s[r][c]
    for dd in corr[p][d]:
        dr,dc=dirs[dd]
        todo.append((r+dr,c+dc,dd))
print(len({(r,c) for r,c,d in found}))
def proc(s,r,c,d):
    h=len(s)
    w=len(s[0])
    todo=[(r,c,d)]
    found=set()
    dirs={'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)}
    corr={'.':{i:i for i in 'RLUD'},
          '\\':{'R':'D','D':'R','L':'U','U':'L'},
          '/':{'R':'U','U':'R','L':'D','D':'L'},
          '|':{'R':'UD','L':'UD','U':'U','D':'D'},
          '-':{'R':'R','L':'L','D':'LR','U':'LR'}}
    while todo:
        t=todo.pop()
        r,c,d=t
        if t in found:continue 
        if c<0 or c>=w or r<0 or r>=h:continue
        found.add(t)
        p=s[r][c]
        for dd in corr[p][d]:
            dr,dc=dirs[dd]
            todo.append((r+dr,c+dc,dd))
    return len({(r,c) for r,c,d in found})

m=0
for i in range(h):
    m=max(m,proc(s,i,0,'R'))
    m=max(m,proc(s,i,w-1,'L'))
for i in range(w):
    m=max(m,proc(s,0,i,'D'))
    m=max(m,proc(s,h-1,i,'U'))
print(m)
