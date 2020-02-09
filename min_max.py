n=int(input())
q=[]
l=list(map(int,input().split()))
c=sum()
for i in range(n):
    k=0
    k=c-l[i]
    q.append(k)
list.sort(q)
print(q[0],q[-1])


######
n=int(input())
q=[]
l=list(map(int,input().split()))
c=sum(l)
list.sort(l)
print(c-l[-1],c-l[0])
