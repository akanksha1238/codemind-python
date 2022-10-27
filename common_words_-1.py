l1=list(map(str,input().split()))
for i in range(len(l1)):
    l1[i] = l1[i].lower()
l2=list(map(str,input().split()))
for i in range(len(l2)):
    l2[i] = l2[i].lower()
n=len(l1)
c=0
for i in l1:
    if i not in l2:
        c=c+1
print(n-c)