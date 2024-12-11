s=INPUT.split('\n')
memo={}
def f(p,l):
    if (p,l) in memo:return memo[(p,l)]
    if not l:return 0 if '#' in p else 1
    if len(p)<l[0]:return 0
    if p[0]=='.':
        ans = f(p[1:],l)
        memo[(p,l)]=ans
        return ans
    if p[0]=='#':
        if all(p[i] in '?#' for i in range(l[0])) and \
            (len(p)==l[0] or p[l[0]] in '.?'):
            ans = f(p[l[0]+1:],l[1:])
            memo[(p,l)]=ans
            return ans
        memo[(p,l)]=0
        return 0
    else:
        ans = f('.'+p[1:],l)+f('#'+p[1:],l)
        memo[(p,l)]=ans
        return ans

tot=0
for i in s:
    p,t=i.split()
    l=tuple(map(int,t.split(',')))
    tot+=f(p,l)
print(tot)

tot=0
for i in s:
    p,t=i.split()
    p=((p+'?')*5)[:-1]
    l=tuple(map(int,t.split(',')))
    l=l*5
    tot+=f(p,l)
print(tot)
