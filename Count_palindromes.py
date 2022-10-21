n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    i=str(i)
    if i==i[::-1]:
        c=c+1
print(c)