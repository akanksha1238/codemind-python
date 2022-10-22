s=input()
s1=s.split(" ")
l=["a","e","i","o","u"]
l1=[]
c=0
for i in s1:
    c=0
    #print(i)
    for j in i:
        if j in l:
            c+=1
    print(c,end=" ")
#print(c)