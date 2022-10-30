n=int(input())
for i in range(n):
    m=input()
    #print(m)
    k=[]
    for i in m:
        k.append(int(i))
    z=min(k)
    x=len(m)
    l=0
    for i in range(z,z+x):
        l=l+i
    if(l==sum(k)):
        print("YES")
    else:
        print("NO")