n=int(input())
l=list(map(str,input().split()))
k=[]
for i in l:
    k.append(int(i))
mi=min(k)
mi=str(mi)
le=len(mi)
c=0
for i in l:
    if len(i)==le:
        c=c+1
print(c)