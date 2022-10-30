n=int(input())
c=0
d=0
a=[]
for i in range(n):
    t=int(input())
    a.append(t)
l=int(input())
for i in range(n):
    if a[i]>l:
        c+=2
    else:
        d+=1
print(c+d)