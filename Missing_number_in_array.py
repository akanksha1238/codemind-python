n=int(input())
for i in range(n):
    s=int(input())
    l=list(map(int,input().split()))
    #print(l)
    z=max(l)
    k=[]
    ll=list(range(1,z+1))
    for i in ll:
        if i not in l:
            k.append(i)
    if(k==[]):
        print(max(l)+1)
    else:
        print(*k)