a,b=map(int,input().split())
k=[]
for i in range(a):
    l=list(map(int,input().split()))
    #print(l)
    s=0
    for i in l:
        s=s+i
    k.append(s)
print(max(k))