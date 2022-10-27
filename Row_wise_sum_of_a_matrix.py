a,b=map(int,input().split())
for i in range(a):
    l=list(map(int,input().split()))
    s=0
    for i in l:
        s=s+i
    print(s,end=" ")