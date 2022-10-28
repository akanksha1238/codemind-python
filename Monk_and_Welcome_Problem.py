n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    res=a[i]+b[i]
    c.append(res)
for i in c:
    print(i,end=" ")