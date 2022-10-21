n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
z=[]
for i in l:
    if(i>=a and i<=b):
        z.append(i)
if(z==[]):
    print(-1)
else:
    print(max(z))