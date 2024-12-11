s=INPUT.split('\n')

def fd(l):
    if len(l)==1:return l[0]
    else:return l[-1]+fd([j-i for i,j in zip(l,l[1:])])

t=0
for i in s:
    l=list(map(int,i.split()))
    t+=fd(l)
print(t)
t=0
for i in s:
    l=list(map(int,i.split()))
    t+=fd(l[::-1])
print(t)
