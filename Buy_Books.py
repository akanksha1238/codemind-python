n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
z1=sum(l1)
z2=sum(l2)
if z2-z1>0:
    print(z2-z1)
else:
    print(0)