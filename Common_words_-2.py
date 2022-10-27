n=list(map(str,input().split()))
m=list(map(str,input().split()))
#print(n,m)
k=[]
kk=[]
for i in n:
    k.append(i.lower())
for i in m:
    kk.append(i.lower())

c=0
for i in k:
    if k.count(i)==1:
        if i in kk:
            if kk.count(i)==1:
                c=c+1
print(c)  