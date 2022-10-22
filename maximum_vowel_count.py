s=input()
s1=s.split(" ")
l=["a","e","i","o","u"]
l1=[]
ma=-1
c=0
for i in s1:
    c=0
    for j in i:
        if j in l:
            c+=1
    if c>ma:
        ma=c
print(ma)