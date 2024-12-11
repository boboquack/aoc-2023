s=INPUT.split('\n')
t=0
v=0
d={i:1 for i in range(len(s)+1)}
n=0
for i in s:
 j=i.split(': ')
 n+=1
 k=j[1].split(' | ')
 a=list(map(int,k[0].split()))
 b=list(map(int,k[1].split()))
 if set(a)&set(b):t+=2**(len(set(a)&set(b))-1)
 if n not in d:break
 v+=d[n]
 for i in range(len(set(a)&set(b))):
  if n+i+1 in d:d[n+i+1]+=d[n]
  else:d[n+i+1]=d[n]
print(t)
print(v)
