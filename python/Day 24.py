s=INPUT.split('\n')
ss='''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''.split('\n')
h=[]
for i in s:
    j,k=i.split(' @ ')
    a,b,c=map(int,j.split(', '))
    d,e,f=map(int,k.split(', '))
    h.append(((a,b,c),(d,e,f)))

def inter(p1,v1,p2,v2):
    #print(p1,v1,p2,v2)
    x1,y1,_=p1
    dx1,dy1,_=v1
    x2,y2,_=p2
    dx2,dy2,_=v2
    if dx1/dx2==dy1/dy2:return False
    # x1+dx1*t=x2+dx2*u
    # y1+dy1*t=y2+dy2*u
    t=((x2-x1)*dy2-(y2-y1)*dx2)/(dx1*dy2-dy1*dx2)
    #print(t)
    xa=x1+dx1*t
    ya=y1+dy1*t
    u=-(x2-x1-dx1*t)/dx2
    #print(xa,ya,t,u)
    #print(u)


    xa=x2+dx2*u
    ya=y2+dy2*u
    #print(xa,ya)
    if t<0 or u<0:return False
    #print('ok')
    return (xa,ya)

def bounds(c):
    x,y=c
    lo,hi=200000000000000,400000000000000
    #lo,hi=7,27
    return lo<=x<=hi and lo<=y<=hi

z=0
for a in range(len(h)):
    for b in range(a+1,len(h)):
        p1,v1=h[a]
        p2,v2=h[b]
        c=inter(p1,v1,p2,v2)
        if c and bounds(c):z+=1
print(z)

'''m=[[0]*9 for i in range(9)]

for i in range(3):
    t='vwx'[i]
    p,v=h[i]
    a,b,c=p
    d,e,f=v
    print(f'{a}{"+" if d>=0 else ""}{d}*{t}=p+s*{t}',end=',')
    print(f'{b}{"+" if d>=0 else ""}{e}*{t}=q+t*{t}',end=',')
    print(f'{c}{"+" if d>=0 else ""}{f}*{t}=r+u*{t}',end=',')
'''

'''
def sim(i,t):
    p,v=h[i]
    a,b,c=p
    d,e,f=v
    print(a+t*d,b+t*e,c+t*f)
'''

'''
eps=1e-10
def deriv(f,x):
    j=1
    while f(x+(abs(x)+1)*(eps*j))==f(x):
        j*=2
        #print(j,x,(abs(x)+1)*(eps*j))
    #print(x,f(x),x+(abs(x)+1)*(eps*j),f(x+abs(x)*(eps*j)))
    return f(x+(abs(x)+1)*(eps*j))-f(x)

BIG=float(10**18)
def minimise(f):
    lo=-BIG
    if deriv(f,lo)>0:return lo,f(lo)
    #print('o')
    hi=BIG
    if deriv(f,hi)<0:return hi,f(hi)
    mid=None
    while hi-lo>eps and mid!=lo and mid!=hi:
        mid=(hi+lo)/2
        if deriv(f,mid)>0:hi=mid
        else:lo=mid 
    return (hi+lo)/2,f((hi+lo)/2)

def dist2(a,b):
    return sum((i-j)**2 for i,j in zip(a,b))
def add(a,b):
    return tuple(i+j for i,j in zip(a,b))
def sca(a,b):
    return tuple(a*i for i in b)
def sub(a,b):
    return tuple(i-j for i,j in zip(a,b))
def distlp(line,point):
    p,v=line
    def f(k):
        return dist2(add(p,sca(k,v)),point)
    return minimise(f)[1]
def distll(line,line2):
    p,v=line
    def f(k):
        return distlp(line2,add(p,sca(k,v)))
    return minimise(f)[1]
def adj(a,b):
    return (*a,b)

#print(distlp(((0,0,0),(0,0,1)),(3,5,4)))

def att(t1):
    p1,v1=h[0]
    #print(t1)
    x1=adj(add(p1,sca(t1,v1)),t1)
    def att2(t2):
        #print('>',t2)
        p2,v2=h[1]
        x2=adj(add(p2,sca(t2,v2)),t2)
        p0=x1
        v0=sub(x2,x1)
        p3,v3=h[2]
        p3=adj(p3,0)
        v3=adj(v3,1)
        d=distll((p0,v0),(p3,v3))
        #print('=',d)
        return (p0,v0),d
    t2=minimise(lambda u:att2(u)[1])[0]
    p0,v0=att2(t2)[0]
    p4,v4=h[3]
    p4=adj(p4,0)
    v4=adj(v4,1)
    return (p0,v0),distll((p0,v0),(p4,v4))
t1=minimise(lambda u:att(u)[1])[0]
p0,v0=att(t1)[0]
print(p0,v0)
'''

'''
def att(t1):
    p1,v1=h[0]
    x1=add(p1,sca(t1,v1))
    def att2(t2):
        if abs(t2-t1)<1e-5:t2=t1+t1/1e-5
        p2,v2=h[1]
        x2=add(p2,sca(t2,v2))
        v0=sca(1/(t2-t1),sub(x2,x1),)
        p0=sub(x1,sca(t1,v1))
        p3,v3=h[2]
        return (p0,v0),distll((p0,v0),(p3,v3))
    t2=minimise(lambda u:att2(u)[1])[0]
    p0,v0=att2(t2)[0]
    p4,v4=h[3]
    return (p0,v0),distll((p0,v0),(p4,v4))
t1=minimise(lambda u:att(u)[1])
p0,v0=att(t1)[0]
print(p0)
'''

from sympy import solve
from sympy.abc import p,q,r,s,t,u,v,w,x

eqs=[]
for i in range(3):
    k=(v,w,x)[i]
    m,n=h[i]
    a,b,c=m
    d,e,f=n
    eqs.append(a+d*k-p-s*k)
    eqs.append(b+e*k-q-t*k)
    eqs.append(c+f*k-r-u*k)
a,b,c,d,e,f,g,h,i=solve(eqs,[p,q,r,s,t,u,v,w,x])[0]
print(a+b+c)

