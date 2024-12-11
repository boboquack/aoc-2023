s=INPUT.split('\n')
d1={'U':(0,1),'R':(1,0),'L':(-1,0),'D':(0,-1)}
x=y=0
a=0
p=0
for i in s:
    d,n,c=i.split()
    n=int(n)
    dx,dy=d1[d]
    x+=dx*n
    y+=dy*n
    a+=dy*n*x
    p+=n
a=abs(a)
# a = p/2+i-1
print(a+p//2+1)
x=y=0
a=0
p=0
d2={'0':'R','1':'D','2':'L','3':'U'}
for i in s:
    d,n,c=i.split()
    n=int(c[2:-2],16)
    d=d2[c[-2]]
    dx,dy=d1[d]
    x+=dx*n
    y+=dy*n
    a+=dy*n*x
    p+=n
a=abs(a)
# a = p/2+i-1
print(a+p//2+1)
