a,b = map(int,input().split())
p=a*b
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
gcd=a
print(p//gcd)
