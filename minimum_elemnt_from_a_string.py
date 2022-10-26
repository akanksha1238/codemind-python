s=input()
s1=s.split(" ")
l=list(s1[len(s1)-1])
l.sort()
o=l[0]
if ord(o)<=95 and ord(o)>=65:
    if o.lower() in l:
        print(o.lower())
    else:
        print(o)
else:
    print(o)