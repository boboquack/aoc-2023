s=INPUT.split('\n\n')
t=0
for i in s:
    j=i.split('\n')
    hr=[k for k in range(len(j)-1) if all(j[k-u]==j[k+1+u] for u in range(min(k,len(j)-2-k)+1))]
    hc=[k for k in range(len(j[0])-1) if all(j[t][k-u]==j[t][k+1+u] for t in range(len(j)) for u in range(min(k,len(j[0])-2-k)+1))]
    if hr:
        t+=(hr[0]+1)*100
    else:
        t+=hc[0]+1
print(t)

def all_but_one(g):
    l=list(g)
    return sum(l)==len(l)-1

t=0
for i in s:
    j=i.split('\n')
    hr=[k for k in range(len(j)-1) if all_but_one(j[k-u][t]==j[k+1+u][t] for t in range(len(j[0])) for u in range(min(k,len(j)-2-k)+1))]
    hc=[k for k in range(len(j[0])-1) if all_but_one(j[t][k-u]==j[t][k+1+u] for t in range(len(j)) for u in range(min(k,len(j[0])-2-k)+1))]
    if hr:
        t+=(hr[0]+1)*100
    else:
        t+=hc[0]+1
print(t)
