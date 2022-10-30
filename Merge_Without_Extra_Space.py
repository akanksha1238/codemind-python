n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    l.extend(l1)
    l.sort()
    print(*l)