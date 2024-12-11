s=INPUT.split()
d={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
t=0
for i in s:
    j=''.join(k for k in i if k.isnumeric())
    t+=int(j[0]+j[-1])
print(t)
t=0
for i in s:
    for u in d:i=i.replace(u,u+d[u]+u)
    j=''.join(k for k in i if k.isnumeric())
    t+=int(j[0]+j[-1])
print(t)
