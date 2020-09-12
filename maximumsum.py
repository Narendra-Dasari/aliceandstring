n=int(input())
q=[]
l=list(map(int,input().split()))
for i in l:
    if i>=0:
        q.append(i)
if len(q)==0:
    print(max(l),1)
else:
    print(sum(q),len(q))
