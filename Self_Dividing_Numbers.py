a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    c=0
    while t>0:
        r=t%10
        if r==0 or i%r!=0:
            c+=1
            break
        t=t//10
    if c==0:
        print(i,end=" ")