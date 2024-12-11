s=INPUT.split('\n')
d={}
for i in s:
    j,k=i.split(': ')
    for l in k.split(' '):
        if j not in d:d[j]=set()
        d[j].add(l)
        if l not in d:d[l]=set()
        d[l].add(j)

l=[i for i in d]

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow

graph=csr_matrix([[int(l[i] in d[l[j]]) for i in range(len(l))] for j in range(len(l))])

import random
while True:
    a=random.randint(0,len(l)-1)
    b=random.randint(0,len(l)-1)
    if a==b:continue
    flow=maximum_flow(graph,a,b)
    if flow.flow_value==3:break
x=[a]
y=[b]
#print(l[a],l[b])
for i in range(len(l)):
    if i==a or i==b:continue
    flow=maximum_flow(graph,a,i)
    if flow.flow_value==3:
        y.append(i)
    else:
        x.append(i)
print(len(x)*len(y))
