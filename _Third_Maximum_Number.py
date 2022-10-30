n=int(input())
l1=list(map(int,input().split()))
l=list(set(l1)) 
l.sort()
l=l[::-1]
if len(l)>=3:
    print(l[2])
elif len(l)==2:
    print(l[0])
elif len(l)==1:
    print(l[0])
else:
    print(0)