s=input()
l=["a","e","i","o","u"]
l1=[]
c=0
for i in l:
    if i not in s:
        print(i,end=" ")
    else:
        
        c+=1
if c==5:
    print(0)