s=input()
s1=s.lower()
d={}
for i in s1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
s=""
l=[]
for k,v in d.items():
    if v==1:
        l.append(k)
l.sort()
for i in l:
    if i==" ":
        l=0
    else:
        s+=i
print(s)