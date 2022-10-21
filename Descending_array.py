n=int(input())
l=list(map(int,input().split()))
flag=True
i=1
while i<len(l):
    if l[i]>l[i-1]:
        flag=False
    i+=1
if flag==True:
    print("yes")
else:
    print("no")