s=input()
s2=s.split(" ")
for s1 in s2:
    k=list(s1)
    
    k.sort()
    o=ord(k[len(k)-1])-ord(k[0])
    print(o,end=" ")