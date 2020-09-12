t=int(input())
l=[]
for i in range(t):
    s=str(input())
    l.append(s)
for i in l:
    if i[::-1] in l:
        print(len(i),i[(len(i)//2)])
        break
