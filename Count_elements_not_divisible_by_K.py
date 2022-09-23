n,k = map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for i in a:
    if i%k!=0:
        cnt+=1
print(cnt)