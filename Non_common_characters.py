n=input()
m=input()
n=n.lower()
m=m.lower()
l=[]
ll=[]
for i in n:
    l.append(i)
for i in m:
    ll.append(i)
k=[]
for i in l:
    if i not in ll:
        k.append(i)
for i in ll:
    if i not in l:
        k.append(i)
l="abcdefghijklmnopqrstuvwxyz"
c=0
for i in l:
    if i in k:
        c=c+1
print(c)