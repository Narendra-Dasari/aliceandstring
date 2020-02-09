t=int(input())
q=[]
for i in range(1,t+1):
    n=str(input())
    l=[i for i in n]
    k=list(set(l))
    list.sort(k)
    a,b=int(max(k)),int(min(k))
    if (a-b==len(l)-1) and (len(k)==len(l)):
        q.append('YES')
    else:
        q.append('NO')
for e in q:
    print(e)
