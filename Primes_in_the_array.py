n=int(input())
a=list(map(int,input().split()))
cnt=0
flag=False
for i in a:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                flag=True
                break
        else:
            cnt+=1
print(cnt)