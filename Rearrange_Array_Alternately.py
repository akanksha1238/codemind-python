n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    if(m%2==0):
        z=l[:m//2]
        z=z[::-1]
        zz=l[m//2:]
        k=[]
        for i in range(len(z)):
            k.append(z[i])
            k.append(zz[i])
        k=k[::-1]    
    else:
        g=l.pop()
        k=[]
        m=m-1
        z=l[:m//2]
        z=z[::-1]
        zz=l[m//2:]
        for i in range(len(z)):
            k.append(zz[i])
            k.append(z[i])
        k=k[::-1]
        k.insert(0,g)
    print(*k)