n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt1=0
for i in a:
    cnt=0
    if i==0:
        cnt=1
    if i<0:
        i=i*(-1)
    while i>0:
        r=i%10
        cnt+=1
        i=i//10
    if cnt==k:
        cnt1+=1
print(cnt1)