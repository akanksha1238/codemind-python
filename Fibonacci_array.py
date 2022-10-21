n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(2,n-2):
    if l[i]==l[i-1]+l[i-2]:
        c=c+1

if c+4==len(l):
    print("yes")
else:
    print("no")