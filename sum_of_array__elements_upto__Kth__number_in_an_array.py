n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in a:
    if i==k:
        s+=i
        break
    else:
        s+=i
print(s)