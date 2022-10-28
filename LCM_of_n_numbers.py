def gcd(n1,n2):
    while n1!=n2:
        if n1>n2:
            n1=n1-n2
        else:
            n2=n2-n1
    return n2
n=int(input())
arr=list(map(int,input().split()))
a=1
for i in arr:
    a=(a*i//gcd(i,a))
print(a)
    