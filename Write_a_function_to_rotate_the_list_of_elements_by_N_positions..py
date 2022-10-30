n=int(input())
l=list(map(int,input().split()))
z=int(input())
for i in range(z):
    j=l.pop()
    l.insert(0,j)
print(*l)