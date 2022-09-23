n,m = map(int,input().split())
r1=list(map(int,input().split()))
r2=list(map(int,input().split()))
a1=set(r1)
a2=set(r2)
cnt=0
for i in a1:
    if i in a2:
        cnt+=1
print(cnt)