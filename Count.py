n=int(input())
l=list(map(int,input().split()))
e=0
d=0
for  i in l:
    if i%2==0:
        e+=1
    else:
        d+=1
print(e,end=" ")
print(d)