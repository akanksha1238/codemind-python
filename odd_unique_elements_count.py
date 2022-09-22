n=int(input())
a=list(map(int,input().split()))
s=set(a)
cnt=0
for i in s:
    if i%2==1:
        cnt+=1
print(cnt)
