s='''62     73     75     65'''.split()
t='''644   1023   1240   1023'''.split()
tt=1
for a,b in zip(s,t):
    a,b=int(a),int(b)
    u=0
    for j in range(a+1):
        if j*(a-j)>b:u+=1
    tt*=u
print(tt)

a=62737565
b=644102312401023

l0=0
h0=a//2
while l0<h0:
    m0=(l0+h0)//2
    if m0*(a-m0)>b:
        h0=m0
    else:
        l0=m0+1
print(a+1-2*(l0))
