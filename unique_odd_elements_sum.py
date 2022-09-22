n=int(input())
a=list(map(int,input().split()))
s=set(a)
s1=0
for i in s:
    if i%2==1:
        s1=s1+i
print(s1)