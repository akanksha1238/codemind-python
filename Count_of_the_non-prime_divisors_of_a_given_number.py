def isprime(n):
    if n==1:
        return 0
    else:
        for i in range(2,n):
            if n%i==0:
                return 0
        else:
            return 1
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        s=isprime(i)
        if s==0:
            c=c+1
print(c)