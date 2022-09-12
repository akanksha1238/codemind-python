n=int(input())
arr=list(map(int,input().split()))
cnt=0
s=sum(arr)
avg=s//n
for i in range(n):
    if arr[i]<=avg:
        cnt+=1
print(cnt)