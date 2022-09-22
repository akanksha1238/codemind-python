n=int(input())
arr=list(map(int,input().split()))
a,b = map(int,input().split())
s=0
for i in arr:
    if i>=a and i<=b:
        s+=i
print(s)