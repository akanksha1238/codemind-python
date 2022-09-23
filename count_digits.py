n=int(input())
a=list(map(int,input().split()))
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
    print(cnt,end=" ")