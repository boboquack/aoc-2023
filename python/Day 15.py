s=INPUT.split(',')

ss=SAMPLE.split(',')



def hash(s):
    t=0
    for i in s:
        t+=ord(i)
        t=t*17%256
    return t

print(sum(hash(i) for i in ss))
print(sum(hash(i) for i in s))

def do(s):
    b=[[] for i in range(256)]
    for i in s:
        if i[-1]=='-':
            j=i[:-1]
            u=hash(j)
            for z in range(len(b[u])):
                if b[u][z][0]==j:
                    b[u]=b[u][:z]+b[u][z+1:]
                    break
        else:
            j,k=i.split('=')
            u=hash(j)
            k=int(k)
            for z in range(len(b[u])):
                if b[u][z][0]==j:
                    b[u][z][1]=k
                    break
            else:
                b[u].append([j,k])
    t=0
    for i in range(len(b)):
        for j in range(len(b[i])):
            t+=(i+1)*(j+1)*b[i][j][1]
    return t
print(do(ss))
print(do(s))

