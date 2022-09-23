m,n=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
ls=[]
for i in a1:
    if i in a2:
        if i not in ls:
            ls.append(i)
for i in ls:
    print(i,end=" ")
        
