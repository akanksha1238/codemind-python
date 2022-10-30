n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)-1):
    h=i+1
    l1=l[h:]
    u=max(l1)
    k.append(u)
k.append(-1)
print(*k)