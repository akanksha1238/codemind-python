n=int(input())
d=c=0
is_prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        is_prime=False
        break
if is_prime==True:
    while n>0:
        flag=True
        rem=n%10
        d+=1
        for i in range(2,int(rem**0.5)+1):
            if rem%i==0:
                flag=False
                break
        if flag==True and rem != 1:
            c+=1
        n=n//10
    if d==c:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
                