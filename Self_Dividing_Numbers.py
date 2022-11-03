a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    t=i
    while t>0:
        rem=t%10
        if rem==0 or i%rem!=0:
            c=1
            break
        t=t//10
    if c==0:
        print(i,end=" ")