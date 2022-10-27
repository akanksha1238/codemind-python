n=input()
n=n.lower()
k=[]
c=0
l='abcdefghijklmnopqrstuvwxyz'
for i in l:
    if i in n:
        c=c+1
print(c==26)