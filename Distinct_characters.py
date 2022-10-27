s=input()
s3=s.replace(" ","")
s1=s3.lower()
n=len
l1=[]
for i in s1:
    l1.append(i)
l1.sort()
s3=set(l1)
l2=list(s3)
l2.sort()

s=""
for i in l2:
    s+=i
print(s)