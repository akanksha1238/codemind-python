n=int(input())
a=0
b=1
cnt=0
while cnt<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    cnt+=1

   