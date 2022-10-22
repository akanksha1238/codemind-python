n=input()
id=input()
k=[]
for i in range(len(n)):
    if n[i]==id:
        k.append(i)
if k==[]:
    print("False")
else:
    print("True")
    print(k[0])