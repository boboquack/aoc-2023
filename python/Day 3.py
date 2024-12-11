s=INPUT.split()
w=len(s[0])
h=len(s)
t=0
f=lambda c:c!='.' and not c.isnumeric()
d={}
for i in range(h):
    for j in range(w):
        if s[i][j].isnumeric() and (j==0 or not s[i][j-1].isnumeric()):
            ok=False
            z=set()
            n=0
            while s[i][j].isnumeric():
                n=n*10+int(s[i][j])
                if j>0 and f(s[i][j-1]):
                    ok=True
                    if s[i][j-1]=='*':z.add((i,j-1))
                if j<w-1 and f(s[i][j+1]):
                    ok=True
                    if s[i][j+1]=='*':z.add((i,j+1))
                if i>0 and f(s[i-1][j]):
                    ok=True
                    if s[i-1][j]=='*':z.add((i-1,j))
                if i<h-1 and f(s[i+1][j]):
                    ok=True
                    if s[i+1][j]=='*':z.add((i+1,j))
                if j>0 and i>0 and f(s[i-1][j-1]):
                    ok=True
                    if s[i-1][j-1]=='*':z.add((i-1,j-1))
                if j<w-1 and i>0 and f(s[i-1][j+1]):
                    ok=True
                    if s[i-1][j+1]=='*':z.add((i-1,j+1))
                if j>0 and i<w-1 and f(s[i+1][j-1]):
                    ok=True
                    if s[i+1][j-1]=='*':z.add((i+1,j-1))
                if j<w-1 and i<w-1 and f(s[i+1][j+1]):
                    ok=True
                    if s[i+1][j+1]=='*':z.add((i+1,j+1))
                j+=1
                if j==w:break
            if ok:
                t+=n
                for u in z:
                    if u in d:d[u].append(n)
                    else:d[u]=[n]
print(t)
p=0
for i in d:
    if len(d[i])==2:
        p+=d[i][0]*d[i][1]
print(p)
