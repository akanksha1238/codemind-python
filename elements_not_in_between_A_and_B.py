n=int(input())
arr=list(map(int,input().split()))
a,b = map(int,input().split())
cnt=0
for i in range(n):
    if arr[i]<a or arr[i]>b:
        print(arr[i],end=" ")
        cnt+=1
if cnt==0:
    print("-1")

