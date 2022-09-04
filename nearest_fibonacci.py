n=int(input())
a=1
b=1
while 2*n>a+b:
    a,b=b,a+b
if (n-a)==(b-n):
    print(a,b)
else:
    print(a)
