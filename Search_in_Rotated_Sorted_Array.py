n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=[]
for i in range(len(l)):
    if l[i]==m:
        k.append(i)
if(k==[]):
    print(-1,)
else:
    print(k[0])