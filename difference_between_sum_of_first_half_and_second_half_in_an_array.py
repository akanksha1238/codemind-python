n=int(input())
a=list(map(int,input().split()))
h=n//2
s1=s2=0
for i in a:
    if i==a[h-1]:
        s1+=i
        break
    else:
        s1+=i
for i in a:
    if i>=a[h]:
        s2+=i
print(abs(s1-s2))