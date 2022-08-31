n=int(input())
a=list(map(int,input().split()))
Sum=0
for i in range(n):
    if a[i]%2==1:
        Sum+=a[i]
print(Sum)
    