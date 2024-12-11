s=INPUT.split('\n')

t=0
for i in s:
    j=i.split(': ')
    n=int(j[0].split()[1])
    u=j[1].split('; ')
    for c in u:
        x = c.split(', ')
        r=0
        g=0
        b=0
        for v in x:
            w=v.split()
            if w[1]=='red':r+=int(w[0])
            if w[1]=='green':g+=int(w[0])
            if w[1]=='blue':b+=int(w[0])
        if r>12 or g>13 or b>14:break
    else:
        t+=n
print(t)
t=0
for i in s:
    j=i.split(': ')
    n=int(j[0].split()[1])
    u=j[1].split('; ')
    rr=0
    gg=0
    bb=0
    for c in u:
        x = c.split(', ')
        r=0
        g=0
        b=0
        for v in x:
            w=v.split()
            if w[1]=='red':r+=int(w[0])
            if w[1]=='green':g+=int(w[0])
            if w[1]=='blue':b+=int(w[0])
        rr=max(r,rr)
        gg=max(g,gg)
        bb=max(b,bb)
    t+=rr*gg*bb
print(t)
