s=input()
s1=s.lower()
l=["a","e","i","o","u"]
l1=[]
c=0
for i in l:
    if i not in s:
        pass
    else:
        c+=1
if c==5:
  print("True")  
else:
    print("False")