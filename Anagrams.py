n=input()
m=input()
n=n.lower()
m=m.lower()
c=0

for i in n:
    if i in m:
        c=c+1
print(c==len(n))