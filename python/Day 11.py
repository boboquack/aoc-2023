s=INPUT.split('\n')

h=len(s)
w=len(s[0])
er=[i for i in range(h) if all(j=='.' for j in s[i])]+[float('inf')]
ec=[i for i in range(w) if all(s[j][i]=='.' for j in range(h))]+[float('inf')]
p=[(i,j) for i in range(h) for j in range(w) if s[i][j]=='#']
rs=sorted(i for i,j in p)
cs=sorted(j for i,j in p)
t=0
j=0
k=0
n=len(rs)
for i in range(n):
 while er[j]<rs[i]:j+=1
 while ec[k]<cs[i]:k+=1
 t+=(2*i-n+1)*(rs[i]+j+cs[i]+k)
print(t)
t=0
j=0
k=0
n=len(rs)
for i in range(n):
 while er[j]<rs[i]:j+=1
 while ec[k]<cs[i]:k+=1
 t+=(2*i-n+1)*(rs[i]+cs[i]+(j+k)*999999)
print(t)
