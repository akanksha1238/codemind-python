n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
z=[]
c=0
for i in l:
    if(i>=a and i<=b):
        c=1
        z.append(i)
if c==0:
    print("-1")
else:
    for i in z:
        print(i,end=" ")
        