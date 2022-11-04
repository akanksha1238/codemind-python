def isprime(n):
    if n==1:
        return 0
    else:
        for i in range(2,n):
            if n%i==0:
                return 0
        else:
            return 1
def rev(n):
    r=0
    while(n>0):
        k=n%10
        r=r*10+k
        n=n//10
    return r
n=int(input())
for i in range(n+1,n+10000):
    s=i
    t=rev(i)
    if s==t:
        l=isprime(s)
        if l==1:
            print(s)
            break