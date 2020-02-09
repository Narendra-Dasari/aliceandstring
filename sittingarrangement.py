t=int(input())
z=[]
for _ in range(t):
    n=int(input())
    c,w,e=0,[],0
    l=["WS","MS","AS","AS","MS","WS"]
    for i in range(1,n+1,6):
        e=e+1
    while c<n:
        m=-1
        for i in range(len(l)):
            m=m+1
            c=c+1
            if c==n:
                break
    if e%2==1:
        if m==0:n=n+11
        elif m==1:n=n+9
        elif m==2:n=n+7
        elif m==3:n=n+5
        elif m==4:n=n+3
        elif m==5:n=n+1
    else:
        if m==5:n=n-11
        elif m==4:n=n-9
        elif m==3:n=n-7
        elif m==2:n=n-5
        elif m==1:n=n-3
        elif m==0:n=n-1
    z.append(n)
    z.append(l[m])
for j in range(0,len(z),2):
    print(z[j],z[j+1])
