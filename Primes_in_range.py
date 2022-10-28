def isPrime(n):
    c=0
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                c+=1
                break
        if c==0:
            return True
        else:
            return False
a=int(input())
b=int(input())
cnt=0
for i in range(a,b+1):
    if isPrime(i)==True:
        cnt+=1
print(cnt)
            