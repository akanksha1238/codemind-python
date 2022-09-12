n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(n):
    if i%2==0 and arr[i]%2!=0:
        cnt+=1
if cnt==0:
    print("True")
else:
    print("False")