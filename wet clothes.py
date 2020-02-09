n,m,g=map(int,input().split())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
q=[]
p=0
for i in range(len(t)-1):
    c=abs(t[i]-t[i+1])
    q.append(c)
k=max(q)
for j in a:
    if j<=k:
        p=p+1
print(p)
