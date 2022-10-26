s2=input()
s1=s2.split(" ")
l=["a","e","i","o","u","A","E","I","O","U"]
l1=[]
c=0
#s=s.replace(" ","@")
for s in s1:
    for i in range((len(s)//2)):
        if s[i] in l and s[(len(s)-1)-i] not in l and s[(len(s)-1)-i]!=" " or s[i] not in l and s[(len(s)-1)-i] in l and s[i]!=" " :
            c+=1
print(c)