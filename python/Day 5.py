seeds=[int(i) for i in INPUT1.split()]

seedsoil=[tuple(map(int,i.split())) for i in INPUT2.split('\n')]

soilfert=[tuple(map(int,i.split())) for i in INPUT3.split('\n')]

fertwat=[tuple(map(int,i.split())) for i in INPUT4.split('\n')]

watlight=[tuple(map(int,i.split())) for i in INPUT5.split('\n')]

lighttemp=[tuple(map(int,i.split())) for i in INPUT6.split('\n')]

temphum=[tuple(map(int,i.split())) for i in INPUT7.split('\n')]

humloc=[tuple(map(int,i.split())) for i in INPUT8.split('\n')]

cycle='seed soil fert wat light temp hum loc'.split()

def lookup(n,m):
    for i,j,k in m:
        if j<=n<j+k:return n-j+i
    return n

m=float('inf')
for i in seeds:
    for j,k in zip(cycle,cycle[1:]):
        mp=eval(j+k)
        i=lookup(i,mp)
    m=min(m,i)
print(m)

def lookup(r,m):
    a,b=r
    for i,j,k in m:
        if j<=a and b<j+k:return [(a-j+i,b-j+i)]
        if j<=a<j+k:return [(a-j+i,i+k-1)]+lookup((j+k,b),m)
        if j<=b<j+k:return [(i,b-j+i)]+lookup((a,j-1),m)
        if a<j and j+k<=b:return [(i,i+k-1)]+lookup((a,j-1),m)+lookup((j+k,b),m)
    return [(a,b)]

def lookups(rs,m):
    u=[lookup(r,m) for r in rs]
    a=[]
    for i in u:a+=i
    return a

m=float('inf')
for i in range(len(seeds)//2):
    x,y=seeds[i*2],seeds[i*2+1]
    v=[(x,x+y-1)]
    for j,k in zip(cycle,cycle[1:]):
        mp=eval(j+k)
        v=lookups(v,mp)
    for i in v:
        m=min(m,i[0])
print(m)
