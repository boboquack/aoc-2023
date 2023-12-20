s='''&ls -> fg, ck, fv, sk, fl, hz
%px -> ls, dv
%jk -> xt, tx
%hd -> fs, vn
%pk -> ql
%bj -> tx, pr
%vg -> xl, sf
%cj -> bj
%sk -> bz
%fl -> fx
%th -> fl, ls
%pr -> gm
%xv -> sf, hp
%mh -> jb
%jh -> kx, tx
%jz -> pm, fs
%hr -> tx, gk
%kx -> cj
%ql -> jx
%gm -> tx, jt
%hz -> ls, fv
%dt -> fs
%gg -> sf, vg
%xl -> fh
&pq -> vr
%jx -> mv
%kr -> gg
%bn -> px, ls
&fs -> pm, rg, pq, pj, nk, mh, jb
%vn -> rt, fs
%jt -> tx, zb
broadcaster -> hz, hr, nk, nv
%fx -> sk, ls
%rt -> fs, kz
%gk -> tx, jh
%mv -> sf, kr
%bz -> bn, ls
%dv -> ls
%rg -> jz
%pj -> mh
%kz -> dt, fs
%ck -> hg
&fg -> vr
&sf -> pk, jx, nv, kr, xl, ql, dk
%jb -> rg
%nk -> fs, pj
&dk -> vr
%hp -> sf
&tx -> hr, fm, kx, cj, pr
%nv -> pk, sf
%fh -> xv, sf
%xt -> tx
%hg -> ls, th
%zb -> tx, jk
&fm -> vr
%pm -> hd
%fv -> ck
&vr -> rx'''.split('\n')
d={}
state={}
for i in s:
    a,b=i.split(' -> ')
    if a!='broadcaster':
        d[a[1:]]=(a[0],b.split(', '))
        if a[0]=='%':
            state[a[1:]]=0
        else:
            state[a[1:]]={}
    else:
        d['broadcaster']=('!',b.split(', '))
for i in d:
    a,b=d[i]
    for j in b:
        if j in state and type(state[j])==dict:state[j][i]=0
lo=0
hi=0
for i in range(1000):
    queue=[('broadcaster',0,'button')]
    while queue:
        x,y,z=queue.pop(0)
        #print(x,y,z)
        if y:hi+=1
        else:lo+=1
        if x not in d:continue
        a,b=d[x]
        if a=='!':
            for i in b:
                queue.append((i,0,x))
        elif a=='%':
            if y==0:
                state[x]^=1
                for i in b:
                    queue.append((i,state[x],x))
        elif a=='&':
            state[x][z]=y
            if all(state[x][i]==1 for i in state[x]):
                o=0
            else:
                o=1
            for i in b:
                queue.append((i,o,x))
print(lo*hi)

for i in s:
    a,b=i.split(' -> ')
    if a!='broadcaster':
        d[a[1:]]=(a[0],b.split(', '))
        if a[0]=='%':
            state[a[1:]]=0
        else:
            state[a[1:]]={}
    else:
        d['broadcaster']=('!',b.split(', '))
for i in d:
    a,b=d[i]
    for j in b:
        if j in state and type(state[j])==dict:state[j][i]=0

import math
print(math.lcm(0b111101011001,0b111110100111,0b111110100001,0b111011010001))

import time
time.sleep(5)
y=set()
x=['broadcaster']
while x:
    i=x.pop()
    if i in y:continue
    y.add(i)
    if i in d:
        a,b=d[i]
        print(i,a,b)
        for j in b[::-1]:x.append(j)

look='nv pk ql jx mv kr gg vg xl fh xv hp sf dk vr'.split()
t=0
#e={}
def on(s):
    if type(state[s])==dict:return int(not all(state[s][j] for j in state[s]))
    return state[s]
while True:
    t+=1
    queue=[('broadcaster',0,'button')]
    s=[]
    while queue:
        x,y,z=queue.pop(0)
        s.append(z)
        if x=='rx' and y==0:
            print(t)
        if x not in d:continue
        a,b=d[x]
        if a=='!':
            for i in b:
                queue.append((i,0,x))
        elif a=='%':
            if y==0:
                state[x]^=1
                for i in b:
                    queue.append((i,state[x],x))
        elif a=='&':
            state[x][z]=y
            if all(state[x][i]==1 for i in state[x]):
                o=0
            else:
                o=1
            for i in b:
                queue.append((i,o,x))
    #for i in state['vr']:
    #    if (type(state[i])==int and state[i]) or (type(state[i])==dict and not all(state[i][j] for j in state[i])):
    #        e[i].append(t)
    #        print(i,t)
    print(t,''.join(str(on(i)) for i in look))

