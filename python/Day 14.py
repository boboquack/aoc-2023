s=INPUT.split()
h=len(s)
w=len(s[0])
t=0
for i in range(w):
 v=h
 for j in range(h):
  if s[j][i]=='O':
   t+=v
   v-=1
  if s[j][i]=='#':
   v=h-j-1
print(t)
def rise(t):
 w=len(t[0])
 h=len(t)
 u=[[i if i!='O' else '.' for i in j] for j in t]
 for i in range(w):
  v=0
  for j in range(h):
   if t[j][i]=='O':
    u[v][i]='O'
    v+=1
   if t[j][i]=='#':
    v=j+1
 return [''.join(j) for j in u]
def spin(t):
 return [''.join(reversed(i)) for i in zip(*t)]
f=lambda t:spin(rise(t))
g=lambda t:f(f(f(f(t))))
d={0:s}
z={tuple(s):0}
N= 1000000000
for i in range(1,N+1):
 s=g(s)
 if tuple(s) in z:break
 d[i]=s
 z[tuple(s)]=i
if i==N:
 a=s
else:
 a=d[(N-i)%(i-z[tuple(s)])+z[tuple(s)]]
t=0
for i in range(h):
 t+=(h-i)*a[i].count('O')
print(t)
