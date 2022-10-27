n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.split()
m=m.split()
for i in m:
    if i in n:
        print(i,end=" ")