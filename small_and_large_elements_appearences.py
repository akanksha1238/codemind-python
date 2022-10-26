s=input()
s=s.replace(" ","")
s1=list(s)
s1.sort()
#print(s1)
a=s1[0]
a1=s1.count(s1[0])
b=s1[len(s1)-1]
b1=s1.count(s1[len(s1)-1])
print(a,a1,b,b1)