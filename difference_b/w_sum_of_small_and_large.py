s=input()
s2=s.split(" ")
o=[]
o1=[]
for s1 in s2:
    k=list(s1)
    
    k.sort()
    o.append(ord(k[len(k)-1]))
    o1.append(ord(k[0]))
print((sum(o)-sum(o1)))