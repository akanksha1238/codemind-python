s=input()
s2=s.split(" ")
for s1 in s2:
    k=list(s1)
    
    k.sort()
    print(k[0],k[len(k)-1],end=" ")