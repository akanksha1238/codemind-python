def gcd(n1,n2):
    if n2%n1==0:
        return n1
    else:
        while n1!=n2:
            if n1>n2:
                n1=n1-n2
            else:
                n2=n2-n1
        return n2
n=int(input())
arr=list(map(int,input().split()))
a=0
for i in arr:
    a=gcd(i,a)
print(a)
    