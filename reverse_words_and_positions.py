n=input()
l=n.split()
l2=l[::-1]
l1=[]
for i in range(len(l)):
    s=l2[i][::-1]
    l1.append(s)
print(*l1)