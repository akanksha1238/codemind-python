n=int(input())
l=[]
z=0
for i in range(n):
    for j in range(n):
        if(i*j==n):
            l.append(i)
            l.append(j)
            z=z+1
if(z!=0):
    print(l[0],end=" ")
    print(l[1])
else:
    print(-1)