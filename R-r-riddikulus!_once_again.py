n,m=map(int,input().split())
l=list(map(int,input().split()))
for i in range(m):
    m=l[0]
    l.remove(m)
    l.append(m)
print(*l)