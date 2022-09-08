n=int(input())
a=0
b=1
c=0
cnt=0
if n==1 or n==0 :
    print("True")
else:
    while c<=n:
        c=a+b
        a=b
        b=c
        if c==n:
            cnt+=1
            print("True")
if cnt==0:
    print("False")
            
        
        
        
        